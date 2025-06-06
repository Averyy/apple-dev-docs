# quadrilateralPoints()

**Framework**: PDFKit  
**Kind**: method

Gets the array of quadrilateral points defining the bounds of the markup.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func quadrilateralPoints() -> [Any]!
```

#### Discussion

Each quadrilateral encompasses a word or a contiguous group of words. The quadrilateral points are ordered counterclockwise, with the first point closest to the origin in page space.

Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page.

## See Also

- [func setQuadrilateralPoints([Any]!)](pdfannotationmarkup/setquadrilateralpoints(_:).md)
  Sets the array of quadrilateral points defining the bounds of the markup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationmarkup/quadrilateralpoints())*