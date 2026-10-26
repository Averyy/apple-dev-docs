# CGPDFDocumentGetMediaBox

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns the media box of a page in a PDF document.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

## Declaration

```c
extern CGRect CGPDFDocumentGetMediaBox(CGPDFDocumentRef document, int page);
```

#### Return Value

A rectangle that represents the media box for the specified page, expressed in default PDF user space units (points).

#### Discussion

The replacement function for this one is [`getBoxRect(_:)`](./cgpdfpage/getboxrect%28_%29.md), which gets the rectangle associated with a type of box (art, media, crop, bleed trim) that represents a content region or page dimensions of a PDF page. For more information see [`CGPDFPage`](./cgpdfpage.md).

The media box defines the location and size of the physical medium on which the page is intended to be displayed or printed. For example, if the page size is 8.5 by 11 inches, this function returns the coordinate pairs `(0,0)` and (`612,792)`.

## Parameters

- `document`: The PDF document to examine.
- `page`: An integer that specifies the number of the page to examine.

## See Also

### Getting Page Information
- [CGPDFDocumentGetArtBox](./cgpdfdocumentgetartbox.md)
  Returns the art box of a page in a PDF document.
- [CGPDFDocumentGetBleedBox](./cgpdfdocumentgetbleedbox.md)
  Returns the bleed box of a page in a PDF document.
- [CGPDFDocumentGetCropBox](./cgpdfdocumentgetcropbox.md)
  Returns the crop box of a page in a PDF document.
- [CGPDFDocumentGetRotationAngle](./cgpdfdocumentgetrotationangle.md)
  Returns the rotation angle of a page in a PDF document.
- [CGPDFDocumentGetTrimBox](./cgpdfdocumentgettrimbox.md)
  Returns the trim box of a page in a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdocumentgetmediabox)*