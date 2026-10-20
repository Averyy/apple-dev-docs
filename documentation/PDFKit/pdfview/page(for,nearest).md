# page(for:nearest:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns the page containing a point specified in view coordinates.

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
func page(for point: CGPoint, nearest: Bool) -> PDFPage?
```

*macOS*

```swift
func page(for point: NSPoint, nearest: Bool) -> PDFPage?
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (PDFPage *) pageForPoint:(CGPoint) point nearest:(BOOL) nearest;
```

*macOS*

```objc
- (PDFPage *) pageForPoint:(NSPoint) point nearest:(BOOL) nearest;
```

#### Discussion

Returns `NULL` if there’s no page at the specified point and `nearest` is set to [`false`](../../Swift/false.md).

## See Also

### Converting Page and View Points
- [func convert(CGPoint, to: PDFPage) -> CGPoint](./convert%28_,to%29-9twqk.md)
  Converts a point from view space to page space.
- [func convert(CGRect, to: PDFPage) -> CGRect](./convert%28_,to%29-8cp0c.md)
  Converts a rectangle from view space to page space.
- [func convert(CGPoint, from: PDFPage) -> CGPoint](./convert%28_,from%29-4evlx.md)
  Converts a point from page space to view space.
- [func convert(CGRect, from: PDFPage) -> CGRect](./convert%28_,from%29-9xv1z.md)
  Converts a rectangle from page space to view space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/page(for:nearest:))*