# ImageAttachmentContent

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A type that holds image data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct ImageAttachmentContent
```

#### Overview

You don’t create `ImageAttachmentContent` directly. Instead, use one of the [`Attachment`](./attachment.md) initializers to attach a [`CGImage`](../CoreGraphics/cgimage.md), [`CIImage`](../CoreImage/ciimage.md), [CVPixelBuffer](../CoreVideo/cvpixelbuffer-q2e.md), or image file URL.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Prompt attachments
- [Analyzing images with multimodal prompting](./analyzing-images-with-multimodal-prompting.md)
  Analyze and extract information from images by combining them with descriptive text prompts.
- [struct Attachment](./attachment.md)
  An asset provided to the model.
- [struct ImageReference](./imagereference.md)
  A reference to an image in a session’s transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/imageattachmentcontent)*