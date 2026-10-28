# convert(_:from:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Converts a point from page space to view space.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func convert(_ point: CGPoint, from page: PDFPage) -> CGPoint
```

*macOS*

```swift
func convert(_ point: NSPoint, from page: PDFPage) -> NSPoint
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (CGPoint) convertPoint:(CGPoint) point fromPage:(PDFPage *) page;
```

*macOS*

```objc
- (NSPoint) convertPoint:(NSPoint) point fromPage:(PDFPage *) page;
```

## Discussion

Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page. View space is a coordinate system with the origin at the lower-left corner of the current PDF view.

## See Also

### Converting Page and View Points
- [func page(for: CGPoint, nearest: Bool) -> PDFPage?](./page%28for,nearest%29.md)
  Returns the page containing a point specified in view coordinates.
- [func convert(CGPoint, to: PDFPage) -> CGPoint](./convert%28_,to%29-9twqk.md)
  Converts a point from view space to page space.
- [func convert(CGRect, to: PDFPage) -> CGRect](./convert%28_,to%29-8cp0c.md)
  Converts a rectangle from view space to page space.
- [func convert(CGRect, from: PDFPage) -> CGRect](./convert%28_,from%29-9xv1z.md)
  Converts a rectangle from page space to view space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/convert(_:from:)-4evlx)*