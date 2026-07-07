# ImageAttachmentContent

**Framework**: Foundation Models  
**Kind**: struct

A type that holds image data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ImageAttachmentContent
```

#### Overview

You don’t create `ImageAttachmentContent` directly. Instead, use one of the [`Attachment`](attachment.md) initializers to attach a `CGImage`, `CIImage`, `CVPixelBuffer`, or image file URL.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Analyzing images with multimodal prompting](analyzing-images-with-multimodal-prompting.md)
  Analyze and extract information from images by combining them with descriptive text prompts.
- [struct Attachment](attachment.md)
  An asset provided to the model.
- [struct ImageReference](imagereference.md)
  A reference to an image in a session’s transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/imageattachmentcontent)*