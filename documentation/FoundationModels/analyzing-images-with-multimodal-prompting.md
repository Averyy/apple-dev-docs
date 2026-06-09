# Analyzing images with multimodal prompting

**Framework**: Foundation Models

Analyze and extract information from images by combining them with descriptive text prompts.

#### Overview

The Foundation Models framework supports using text and images in your prompts, giving you the ability to analyze and interpret visual content. When paired with tool calling, this *multimodal prompting* approach makes it possible to build rich content analysis workflows and apps that perform sophisticated image analysis tasks, such as:

- Performing image classification tasks based on the subject matter in an image.
- Summarizing the content within a photo of a document.
- Generating accessibility descriptions for images that you share on the web.
- Identifying a list of items within a photo of a fridge to generate recipe ideas.

#### Prompt an on Device Model with Images

When including an image with a text prompt, the model processes both the visual content and any accompanying text to generate a response. This multimodal approach allows the model to interpret visual details that are difficult to convey through text alone.

To improve the results, consider the following strategies when including an image in your prompt:

- Describe clearly what you want the model to analyze or extract. Instead of asking, “What’s in this image?,” try “List all food items in this photo.”
- Consider whether preprocessing is necessary before passing an image to an on-device model, such as isolating a region of interest.
- Use the [`Generable`](generable.md) protocol to constrain responses to specific formats, making it easier to extract structured data or classify images.

#### Include Images in Your Request

The framework supports several image types to include in your prompts, like [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage), [`CIImage`](https://developer.apple.com/documentation/CoreImage/CIImage), [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/CVPixelBuffer), and image URLs.

Use a URL whenever your image comes from a file and verify that it points to an actual image. The framework infers whether a URL represents an image based on its [`UTType`](https://developer.apple.com/documentation/UniformTypeIdentifiers/UTType-swift.struct). If your app captures images or processes video streams, use [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/CVPixelBuffer).

> ❗ **Important**: The framework performs the necessary scaling and color conversions before passing an image to the model, so you don’t need to scale or convert images to different formats.

To include an image with your text prompt, use the [`Attachment`](attachment.md) structure and specify additional details about the image attachment, like the display orientation of the image. When specifying the orientation, the framework performs a transform before sending the image to the model:

```swift
func compareImages(imageOne: CGImage, imageTwo: CGImage) async throws -> String {
    let session = LanguageModelSession()
    let response = try await session.respond {
        "Compare these two images by using three bullet points:"
        
        Attachment(imageOne)
        
        // When the image doesn't have a rotation applied, like when you get a
        // image from the `AVFoundation` framework, use orientation to perform 
        // a transform before sending it to the model.
        Attachment(imageTwo, orientation: .right)
    }
    return response.content
}
```

Perform image analysis with the on-device model first. If you determine that more reasoning or context is necessary for the task, initialize [`LanguageModelSession`](languagemodelsession.md) using [`PrivateCloudComputeLanguageModel`](privatecloudcomputelanguagemodel.md).

#### Define Custom Types to Perform Image Analysis

For more structured results, use the [`Generable`](generable.md) protocol to create an enumeration with specific labels you use to identify the contents of an image. This approach is useful when you need to classify images into predefined categories, ensuring the model returns one of your specified labels rather than free-form text. For example, the following prompts the model to identify which label best represents the image:

```swift
@Generable
enum ImageLabel {
    case cat
    case dog
    case frog
    case bird
}

func classifyImage(_ image: CGImage) async throws -> ImageLabel {
    let session = LanguageModelSession()
    let response = try await session.respond(
        generating: ImageLabel.self,
        options: GenerationOptions(samplingMode: .greedy)
    ) {
        "Choose the label that best represents the following image:"
        
        Attachment(image)
    }
    return response.content
}
```

> 💡 **Tip**: Use the [`greedy`](generationoptions/samplingmode-swift.struct/greedy.md) sampling option when you want the model to always pick the most likely option; otherwise, the model may select an option that’s close.

For more information on guided generation, see [`Generating Swift data structures with guided generation`](generating-swift-data-structures-with-guided-generation.md).

#### Use Built in Image Analysis Tools

The [`Vision`](https://developer.apple.com/documentation/Vision) framework provides optical character recognition (OCR) and barcode tools that you can add to a session in the Foundation Models framework. Use [`BarcodeReaderTool`](https://developer.apple.com/documentation/Vision/BarcodeReaderTool) to detect barcodes and interpret their encoded content, and [`OCRTool`](https://developer.apple.com/documentation/Vision/OCRTool) to extract text from images.

When you use tools, provide an [`label(_:)`](attachment/label(_:).md) to help the model identify a specific attachment. The following shows how to prompt the model to get information about an image that contains a barcode:

```swift
func analyzeBarcodeImage(_ image: CGImage) async {
    do {
        let session = LanguageModelSession(tools: [BarcodeReaderTool()])
        let response = try await session.respond {
            """
            Scan this image for any barcodes. For each barcode found, describe \
            its symbology type and explain what the encoded content means or \
            represents.
            """
            
            Attachment(image)
                .label("barcode-image")
        }.content
        
        print("The model response: \(response)")
    } catch {
        // Handle the error.
    }
}
```

#### Create a Custom Tool to Perform Image Analysis

Provide custom image processing to the model by creating a custom tool. When you create a tool, you specify the arguments that the model provides when calling your tool. When defining your arguments, use [`ImageReference`](imagereference.md) to receive a reference to your image:

```swift
@Generable
struct Arguments {
    @Guide(description: "The identifier of the image to analyze.")
    var image: ImageReference
}
```

When the model calls your tool, the [`call(arguments:)`](tool/call(arguments:).md) method receives a reference you use to access the image. For example, to create a tool that uses the [`Vision`](https://developer.apple.com/documentation/Vision) framework to get classification details:

```swift
func call(arguments: Arguments) async throws -> String {
    // Get the image attachment from the session history.
    guard let attachment = arguments.image.resolve(in: Transcript(entries: sessionHistory)) else {
        return "The image isn't in the session history."
    }
    
    // Perform a classification request on the image to get the top five 
    // observations.
    let observations = try await ClassifyImageRequest().perform(on: attachment.ciImage)
    let top = observations.prefix(5)
    return top.map { $0.identifier }.joined(separator: ", ")
}
```

For more information on creating tools, see [`Expanding generation with tool calling`](expanding-generation-with-tool-calling.md).

## See Also

- [struct Attachment](attachment.md)
  An asset provided to the model.
- [protocol AttachmentContent](attachmentcontent.md)
  A type that you use as the content of an attachment.
- [struct ImageAttachmentContent](imageattachmentcontent.md)
  A type that holds image data.
- [struct ImageReference](imagereference.md)
  A reference to an image in a session’s transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/analyzing-images-with-multimodal-prompting)*