# getBoxRect(_:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle that represents a type of box for a content region or page dimensions of a PDF page.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func getBoxRect(_ box: CGPDFBox) -> CGRect
```

```c
extern CGRect CGPDFPageGetBoxRect(CGPDFPageRef page, CGPDFBox box);
```

## Return Value

Returns the rectangle associated with the type of box specified by the `box` parameter in the specified page.

## Discussion

Returns the rectangle associated with the specified box in the specified page. This is the value of the corresponding entry (such as `/MediaBox`, `/ArtBox`, and so on) in the page’s dictionary.

## Parameters

- `box`: A constant that specifies the type of box. For possible values, see [`CGPDFBox`](../cgpdfbox.md).

## See Also

### Getting Page Information
- [var dictionary: CGPDFDictionaryRef?](./dictionary.md)
  Returns the dictionary of a PDF page.
- [var document: CGPDFDocument?](./document.md)
  Returns the document for a page.
- [var pageNumber: Int](./pagenumber.md)
  Returns the page number of the specified PDF page.
- [var rotationAngle: Int32](./rotationangle.md)
  Returns the rotation angle of a PDF page, in degrees.
- [func getDrawingTransform(CGPDFBox, rect: CGRect, rotate: Int32, preserveAspectRatio: Bool) -> CGAffineTransform](./getdrawingtransform%28_,rect,rotate,preserveaspectratio%29.md)
  Returns the affine transform that maps a box to a given rectangle on a PDF page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfpage/getboxrect(_:))*