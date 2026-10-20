# setQuadrilateralPoints(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Sets the array of quadrilateral points defining the bounds of the markup.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func setQuadrilateralPoints(_ points: [Any]!)
```

```objc
- (void) setQuadrilateralPoints:(NSArray *) points;
```

#### Discussion

The points defined by each quadrilateral array should encompass a word or a contiguous group of words. The quadrilateral points are ordered counterclockwise, with the first point closest to the origin in page space.

Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page.

## See Also

### Working with Markup Boundaries
- [func quadrilateralPoints() -> [Any]!](./quadrilateralpoints%28%29.md)
  Gets the array of quadrilateral points defining the bounds of the markup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationmarkup/setquadrilateralpoints(_:))*