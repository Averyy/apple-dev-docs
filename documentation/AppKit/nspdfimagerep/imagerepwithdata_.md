# imageRepWithData:

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates and returns a representation of an image initialized with the specified PDF data.

**Availability**:
- macOS

## Declaration

```objc
+ (instancetype) imageRepWithData:(NSData *) pdfData;
```

#### Return Value

An initialized [`NSPDFImageRep`](../nspdfimagerep.md) object, or `nil` if the object could not be initialized. Initialization may fail if the PDF data does not conform to the PDF file format.

## Parameters

- `pdfData`: A data object containing the PDF data for the image.

## See Also

### Related Documentation
- [var pdfRepresentation: Data](./pdfrepresentation.md)
  The PDF representation of the representation’s image.
### Creating Representations of Images from PDF Data
- [init?(data: Data)](./init%28data%29.md)
  Returns a representation of an image initialized with the specified PDF data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspdfimagerep/imagerepwithdata:)*