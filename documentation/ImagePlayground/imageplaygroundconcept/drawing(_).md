# drawing(_:)

**Framework**: Image Playground  
**Kind**: method  
**Role**: Type Method

Creates a concept structure from a PencilKit drawing.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- visionOS 2.4+

## Declaration

```swift
static func drawing(_ drawing: PKDrawing) -> ImagePlaygroundConcept
```

#### Discussion

Call this method when you want to use a PencilKit drawing as the basis for generating a new image. Typically, you include other text-based concept structures in addition to this one. Include at most one PencilKit drawing among a collection of concepts. Including more than one drawing yields unpredictable image results.

## Parameters

- `drawing`: A PencilKit drawing object that contains a set of strokes. The system uses this drawing, along with other concepts, to guide the image creation.

## See Also

### Describing the image
- [static func text(String) -> ImagePlaygroundConcept](./text%28_%29.md)
  Creates a concept structure that includes a short text description.
- [static func extracted(from: String, title: String?) -> ImagePlaygroundConcept](./extracted%28from,title%29.md)
  Creates a concept structure from a long-form string and a title that guides the extraction of concepts from that string.
- [static func image(CGImage) -> ImagePlaygroundConcept](./image%28_%29-29ora.md)
  Creates a concept structure from the specified image object.
- [static func image(URL) -> ImagePlaygroundConcept?](./image%28_%29-2s44c.md)
  Creates a concept structure from the image at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundconcept/drawing(_:))*