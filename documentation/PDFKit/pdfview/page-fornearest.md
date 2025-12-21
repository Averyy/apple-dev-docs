# page(for:nearest:)

**Framework**: PDFKit  
**Kind**: method

Returns the page containing a point specified in view coordinates.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func page(for point: NSPoint, nearest: Bool) -> PDFPage?
```

#### Discussion

Returns `NULL` if there’s no page at the specified point and `nearest` is set to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func convert(CGPoint, to: PDFPage) -> CGPoint](pdfview/convert(_:to:)-9twqk.md)
  Converts a point from view space to page space.
- [func convert(CGRect, to: PDFPage) -> CGRect](pdfview/convert(_:to:)-8cp0c.md)
  Converts a rectangle from view space to page space.
- [func convert(CGPoint, from: PDFPage) -> CGPoint](pdfview/convert(_:from:)-4evlx.md)
  Converts a point from page space to view space.
- [func convert(CGRect, from: PDFPage) -> CGRect](pdfview/convert(_:from:)-9xv1z.md)
  Converts a rectangle from page space to view space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/page(for:nearest:))*