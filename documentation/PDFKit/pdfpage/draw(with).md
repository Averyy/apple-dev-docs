# draw(with:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Draws the page within the specified box.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func draw(with box: PDFDisplayBox)
```

```objc
- (void) drawWithBox:(PDFDisplayBox) box;
```

## Mentions

- [Adding Custom Graphics to a PDF](../adding-custom-graphics-to-a-pdf.md)

## Discussion

This method takes into account the page rotation and draws clipped to the specified box. If the page is set to display annotations, this method also draws them. This method does not clear the background. To clear the background before drawing, use [`NSRectFill`](../../AppKit/nsrectfill.md) with `NSColor` set (typically) to white.

## See Also

### Related Documentation
- [var displaysAnnotations: Bool](./displaysannotations.md)
  Returns a Boolean value indicating whether annotations are displayed for the page.
### Rendering Pages
- [func transformContext(for: PDFDisplayBox)](./transformcontext%28for%29.md)
  Transforms the current context, given the specified box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/draw(with:))*