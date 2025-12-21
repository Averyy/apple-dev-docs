# getDrawingTransform(_:rect:rotate:preserveAspectRatio:)

**Framework**: Core Graphics  
**Kind**: method

Returns the affine transform that maps a box to a given rectangle on a PDF page.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func getDrawingTransform(_ box: CGPDFBox, rect: CGRect, rotate: Int32, preserveAspectRatio: Bool) -> CGAffineTransform
```

#### Return Value

An affine transform that maps the box specified by the `box` parameter to the rectangle specified by the `rect` parameter.

#### Discussion

Quartz constructs the affine transform as follows:

- Computes the effective rectangle by intersecting the rectangle associated with `box` and the `/MediaBox` entry of the specified page.
- Rotates the effective rectangle according to the page’s `/Rotate` entry.
- Centers the resulting rectangle on `rect`.If the value of the `rotate` parameter is non-zero, then the rectangle is rotated clockwise by rotate degrees. The value of `rotate` must be a multiple of 90.
- Scales the rectangle, if necessary, so that it coincides with the edges of `rect`. If the value of `preserveAspectRatio` parameter is [`true`](https://developer.apple.com/documentation/Swift/true), then the final rectangle coincides with the edges of `rect` only in the more restrictive dimension.

## Parameters

- `box`: A constant that specifies the type of box. For possible values, see  .
- `rect`: A Quartz rectangle.
- `rotate`: An integer, that must be a multiple of  , that specifies the angle by which the specified rectangle is rotated clockwise.
- `preserveAspectRatio`: A Boolean value that specifies whether or not the aspect ratio should be preserved. A value of   specifies that the aspect ratio should be preserved.

## See Also

- [func getBoxRect(CGPDFBox) -> CGRect](cgpdfpage/getboxrect(_:).md)
  Returns the rectangle that represents a type of box for a content region or page dimensions of a PDF page.
- [var dictionary: CGPDFDictionaryRef?](cgpdfpage/dictionary.md)
  Returns the dictionary of a PDF page.
- [var document: CGPDFDocument?](cgpdfpage/document.md)
  Returns the document for a page.
- [var pageNumber: Int](cgpdfpage/pagenumber.md)
  Returns the page number of the specified PDF page.
- [var rotationAngle: Int32](cgpdfpage/rotationangle.md)
  Returns the rotation angle of a PDF page, in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfpage/getdrawingtransform(_:rect:rotate:preserveaspectratio:))*