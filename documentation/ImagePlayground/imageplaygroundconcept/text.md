# text(_:)

**Framework**: Image Playground  
**Kind**: method

Creates a concept structure that includes a short text description.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- visionOS 2.4+

## Declaration

```swift
static func text(_ text: String) -> ImagePlaygroundConcept
```

#### Return Value

A concept object that encapsulates the specified text.

#### Discussion

Call this method when you want to use short strings to generate an image. The system passes short strings in their entirety as input to the diffusion model. If you provide a long string, the system tries to extract only the relevant details and pass those to the model instead.

## Parameters

- `text`: The text that describes the image. Your text must be relatively   short, so specify single words or brief sentences. If you specify a   string that exceeds the model’s supported maximum string length, the   system tries to extract important or interesting concepts and use those instead.

## See Also

- [static func extracted(from: String, title: String?) -> ImagePlaygroundConcept](imageplaygroundconcept/extracted(from:title:).md)
  Creates a concept structure from a long-form string and a title that guides the extraction of concepts from that string.
- [static func drawing(PKDrawing) -> ImagePlaygroundConcept](imageplaygroundconcept/drawing(_:).md)
  Creates a concept structure from a PencilKit drawing.
- [static func image(CGImage) -> ImagePlaygroundConcept](imageplaygroundconcept/image(_:)-29ora.md)
  Creates a concept structure from the specified image object.
- [static func image(URL) -> ImagePlaygroundConcept?](imageplaygroundconcept/image(_:)-2s44c.md)
  Creates a concept structure from the image at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundconcept/text(_:))*