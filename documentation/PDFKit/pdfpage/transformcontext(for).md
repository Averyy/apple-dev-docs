# transformContext(for:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Transforms the current context, given the specified box.

**Availability**:
- macOS 10.5+ - Deprecated in 10.12

## Declaration

```swift
func transformContext(for box: PDFDisplayBox)
```

```objc
- (void) transformContextForBox:(PDFDisplayBox) box;
```

## Discussion

When transforming the current context, this method takes into account the rotation of the page, as well as the origin of the box with respect to the page’s base coordinate system. This is a convenient method to call within the `PDFView` [`draw(_:)`](../pdfview/draw%28_%29.md) method or from within a draw method of a `PDFAnnotation` subclass.

## See Also

### Related Documentation
- [class PDFPage](../pdfpage.md)
  `PDFPage`, a subclass of `NSObject`, defines methods used to render PDF pages and work with annotations, text, and selections.
### Rendering Pages
- [func draw(with: PDFDisplayBox)](./draw%28with%29.md)
  Draws the page within the specified box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/transformcontext(for:))*