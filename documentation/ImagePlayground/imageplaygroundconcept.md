# ImagePlaygroundConcept

**Framework**: Image Playground  
**Kind**: struct  
**Role**: Structure

Text elements that specify the content to include in the image.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- visionOS 2.4+

## Declaration

```swift
struct ImagePlaygroundConcept
```

#### Overview

Use this type to wrap pieces of text describing the image you want to create. You can also specify larger pieces of text that contain important concepts to extract and use to guide the image-creation process.

## Topics

### Describing the image
- [static func text(String) -> ImagePlaygroundConcept](./imageplaygroundconcept/text%28_%29.md)
  Creates a concept structure that includes a short text description.
- [static func extracted(from: String, title: String?) -> ImagePlaygroundConcept](./imageplaygroundconcept/extracted%28from,title%29.md)
  Creates a concept structure from a long-form string and a title that guides the extraction of concepts from that string.
- [static func drawing(PKDrawing) -> ImagePlaygroundConcept](./imageplaygroundconcept/drawing%28_%29.md)
  Creates a concept structure from a PencilKit drawing.
- [static func image(CGImage) -> ImagePlaygroundConcept](./imageplaygroundconcept/image%28_%29-29ora.md)
  Creates a concept structure from the specified image object.
- [static func image(URL) -> ImagePlaygroundConcept?](./imageplaygroundconcept/image%28_%29-2s44c.md)
  Creates a concept structure from the image at the specified URL.

## See Also

### Platform support
- [struct ImagePlaygroundStyle](./imageplaygroundstyle.md)
  Style options that determine the appearance of generated images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundconcept)*