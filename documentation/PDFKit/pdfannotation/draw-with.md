# draw(with:)

**Framework**: PDFKit  
**Kind**: method

Draws the annotation on its associated page.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func draw(with box: PDFDisplayBox)
```

## Mentions

- [Adding Custom Graphics to a PDF](adding-custom-graphics-to-a-pdf.md)

#### Discussion

The annotation is drawn relative to the origin of `box` in page-space coordinates.

Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page.

## Parameters

- `box`: The bounding box to draw the annotation in.

## See Also

- [func bounds(for: PDFDisplayBox) -> CGRect](pdfpage/bounds(for:).md)
  Returns the bounds for the specified PDF display box.
- [convenience init(bounds: NSRect)](pdfannotation/init(bounds:).md)
  Creates a PDF annotation object.
- [convenience init(dictionary: [AnyHashable : Any], forPage: PDFPage?)](pdfannotation/init(dictionary:forpage:).md)
- [func removeAllAppearanceStreams()](pdfannotation/removeallappearancestreams.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/draw(with:))*