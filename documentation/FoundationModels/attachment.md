# Attachment

**Framework**: Foundation Models  
**Kind**: struct

An asset provided to the model.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Attachment<Content>
```

## Mentions

- [Analyzing images with multimodal prompting](analyzing-images-with-multimodal-prompting.md)

#### Overview

Use `Attachment` to include media such as images alongside text in your prompts and instructions.

```swift
let response = try await session.respond {
    "Describe this image:"
    Attachment(image)
}
```

Use the [`label(_:)`](attachment/label(_:).md) method to assign a label to an attachment. Labels help the model identify specific attachments when making tool calls.

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
- [init(_:orientation:)](attachment/init(_:orientation:).md)
  Creates an attachment from a Core Graphics image.
- [init(imageURL: URL, orientation: CGImagePropertyOrientation?)](attachment/init(imageurl:orientation:).md)
  Creates an attachment from a file URL pointing to an image.
### Assigning a label
- [func label(String) -> Attachment<Content>](attachment/label(_:).md)
  Assigns a label to an attachment.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [InstructionsRepresentable](instructionsrepresentable.md)
- [PromptRepresentable](promptrepresentable.md)

## See Also

- [Analyzing images with multimodal prompting](analyzing-images-with-multimodal-prompting.md)
  Analyze and extract information from images by combining them with descriptive text prompts.
- [struct ImageAttachmentContent](imageattachmentcontent.md)
  A type that holds image data.
- [struct ImageReference](imagereference.md)
  A reference to an image in a session’s transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/attachment)*