# Attachment

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

An asset provided to the model.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct Attachment<Content>
```

## Mentions

- [Analyzing images with multimodal prompting](./analyzing-images-with-multimodal-prompting.md)

#### Overview

Use `Attachment` to include media such as images alongside text in your prompts and instructions.

```swift
let response = try await session.respond {
    "Describe this image:"
    Attachment(image)
}
```

Use the [`label(_:)`](./attachment/label%28_%29.md) method to assign a label to an attachment. Labels help the model identify specific attachments when making tool calls.

```swift
Prompt {
    "Compare these two images:"
    Attachment(firstImage)
        .label("image-0")
    Attachment(secondImage)
        .label("image-1")
}
```

## Topics

### Creating an attachment instance
- [init(_:orientation:)](./attachment/init%28_,orientation%29.md)
  Creates an attachment from a Core Graphics image.
- [init(imageURL: URL, orientation: CGImagePropertyOrientation?)](./attachment/init%28imageurl,orientation%29.md)
  Creates an attachment from a file URL pointing to an image.
### Assigning a label
- [func label(String) -> Attachment<Content>](./attachment/label%28_%29.md)
  Assigns a label to an attachment.
### Initializers
- [init(Content)](./attachment/init%28_%29.md)
  Creates an attachment from data content.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [InstructionsRepresentable](./instructionsrepresentable.md)
- [PromptRepresentable](./promptrepresentable.md)

## See Also

### Prompt attachments
- [Analyzing images with multimodal prompting](./analyzing-images-with-multimodal-prompting.md)
  Analyze and extract information from images by combining them with descriptive text prompts.
- [struct ImageAttachmentContent](./imageattachmentcontent.md)
  A type that holds image data.
- [struct ImageReference](./imagereference.md)
  A reference to an image in a session’s transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/attachment)*