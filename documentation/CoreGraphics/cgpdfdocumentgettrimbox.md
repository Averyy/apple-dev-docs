# CGPDFDocumentGetTrimBox

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns the trim box of a page in a PDF document.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

## Declaration

```c
extern CGRect CGPDFDocumentGetTrimBox(CGPDFDocumentRef document, int page);
```

## Return Value

Returns a rectangle that represents the trim box for the specified page, expressed in default PDF user space units (points).

## Discussion

The replacement function for this one is [`getBoxRect(_:)`](./cgpdfpage/getboxrect%28_%29.md), which gets the rectangle associated with a type of box (art, media, crop, bleed trim) that represents a content region or page dimensions of a PDF page. For more information see [`CGPDFPage`](./cgpdfpage.md).

The trim box defines the intended dimensions of the finished page after trimming. It may be smaller than the media box, to allow for production-related content such as printing instructions, cut marks, or color bars. The default value is the page’s crop box.

## Parameters

- `document`: The PDF document to examine.
- `page`: A value specifying the number of the page to examine.

## See Also

### Getting Page Information
- [CGPDFDocumentGetArtBox](./cgpdfdocumentgetartbox.md)
  Returns the art box of a page in a PDF document.
- [CGPDFDocumentGetBleedBox](./cgpdfdocumentgetbleedbox.md)
  Returns the bleed box of a page in a PDF document.
- [CGPDFDocumentGetCropBox](./cgpdfdocumentgetcropbox.md)
  Returns the crop box of a page in a PDF document.
- [CGPDFDocumentGetMediaBox](./cgpdfdocumentgetmediabox.md)
  Returns the media box of a page in a PDF document.
- [CGPDFDocumentGetRotationAngle](./cgpdfdocumentgetrotationangle.md)
  Returns the rotation angle of a page in a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdocumentgettrimbox)*