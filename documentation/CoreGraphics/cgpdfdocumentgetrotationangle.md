# CGPDFDocumentGetRotationAngle

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns the rotation angle of a page in a PDF document.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

## Declaration

```c
extern int CGPDFDocumentGetRotationAngle(CGPDFDocumentRef document, int page);
```

## Return Value

The rotation angle of the page, expressed in degrees. If the specified page does not exist, returns `0`.

## Discussion

The replacement function for this one is [`rotationAngle`](./cgpdfpage/rotationangle.md). For more information see [`CGPDFPage`](./cgpdfpage.md).

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
- [CGPDFDocumentGetMediaBox](./cgpdfdocumentgetmediabox.md)
  Returns the media box of a page in a PDF document.
- [CGPDFDocumentGetTrimBox](./cgpdfdocumentgettrimbox.md)
  Returns the trim box of a page in a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdocumentgetrotationangle)*