# CGPDFDocumentGetArtBox

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns the art box of a page in a PDF document.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

## Declaration

```c
extern CGRect CGPDFDocumentGetArtBox(CGPDFDocumentRef document, int page);
```

## Return Value

A rectangle that represents the art box for the specified page, expressed in default PDF user space units (points).

## Discussion

The replacement function for this one is [`getBoxRect(_:)`](./cgpdfpage/getboxrect%28_%29.md), which gets the rectangle associated with a type of box (art, media, crop, bleed trim) that represents a content region or page dimensions of a PDF page. For more information see [`CGPDFPage`](./cgpdfpage.md).

The art box defines the extent of the page’s meaningful content (including potential white space) as intended by the document creator. The default value is the page’s crop box.

## Parameters

- `document`: The PDF document to examine.
- `page`: An integer that specifies the number of the page to examine.

## See Also

### Getting Page Information
- [CGPDFDocumentGetBleedBox](./cgpdfdocumentgetbleedbox.md)
  Returns the bleed box of a page in a PDF document.
- [CGPDFDocumentGetCropBox](./cgpdfdocumentgetcropbox.md)
  Returns the crop box of a page in a PDF document.
- [CGPDFDocumentGetMediaBox](./cgpdfdocumentgetmediabox.md)
  Returns the media box of a page in a PDF document.
- [CGPDFDocumentGetRotationAngle](./cgpdfdocumentgetrotationangle.md)
  Returns the rotation angle of a page in a PDF document.
- [CGPDFDocumentGetTrimBox](./cgpdfdocumentgettrimbox.md)
  Returns the trim box of a page in a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdocumentgetartbox)*