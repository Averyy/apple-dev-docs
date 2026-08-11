# ImageReference

**Framework**: Foundation Models  
**Kind**: struct

A reference to an image in a session’s transcript.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ImageReference
```

## Mentions

- [Analyzing images with multimodal prompting](analyzing-images-with-multimodal-prompting.md)

#### Overview

Use `ImageReference` to allow the model to reference images from the transcript of the current `LanguageModelSession`.

You can define an `ImageReference` as an argument to a `Tool`. Retrieve the referenced image from the transcript during the tool call.

```swift
struct MyTool: Tool {
  @SessionProperty(\.history) var history

  @Generable
  struct Arguments {
    var image: ImageReference
  }

  public func call(arguments: Arguments) async throws -> Output {
    guard let imageAttachment = arguments.image.resolved(in: history) else {
      throw ImageToolError.imageNotFound(arguments.image.attachmentLabel)
    }
    let image = imageAttachment.cgImage
    ...
  }
}
```

## Topics

### Getting the image label
- [let attachmentLabel: String](imagereference/attachmentlabel.md)
  The label of the referenced image.
### Accessing the referenced image
- [func resolved(in: some Sequence<Transcript.Entry>) -> Transcript.ImageAttachment?](imagereference/resolved(in:).md)
  Returns the referenced image from the transcript.

## Relationships

### Conforms To
- [ConvertibleFromGeneratedContent](convertiblefromgeneratedcontent.md)
- [ConvertibleToGeneratedContent](convertibletogeneratedcontent.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Generable](generable.md)
- [InstructionsRepresentable](instructionsrepresentable.md)
- [PromptRepresentable](promptrepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Analyzing images with multimodal prompting](analyzing-images-with-multimodal-prompting.md)
  Analyze and extract information from images by combining them with descriptive text prompts.
- [struct Attachment](attachment.md)
  An asset provided to the model.
- [struct ImageAttachmentContent](imageattachmentcontent.md)
  A type that holds image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/imagereference)*