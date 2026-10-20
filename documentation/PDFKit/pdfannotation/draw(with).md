# draw(with:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Draws the annotation on its associated page.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

> **Deprecated**: Use [`draw(with:in:)`](./draw%28with,in%29.md) instead.

## Declaration

```swift
func draw(with box: PDFDisplayBox)
```

```objc
- (void) drawWithBox:(PDFDisplayBox) box;
```

## Mentions

- [Adding Custom Graphics to a PDF](../adding-custom-graphics-to-a-pdf.md)

#### Discussion

The annotation is drawn relative to the origin of `box` in page-space coordinates.

Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page.

## Parameters

- `box`: The bounding box to draw the annotation in.

## See Also

### Related Documentation
- [func bounds(for: PDFDisplayBox) -> CGRect](../pdfpage/bounds%28for%29.md)
  Returns the bounds for the specified PDF display box.
### Deprecated Methods
- [convenience init(bounds: NSRect)](./init%28bounds%29.md)
  Creates a PDF annotation object.
- [convenience init(dictionary: [AnyHashable : Any], forPage: PDFPage?)](./init%28dictionary,forpage%29.md)
- [func removeAllAppearanceStreams()](./removeallappearancestreams%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/draw(with:))*