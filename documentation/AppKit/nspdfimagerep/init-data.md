# init(data:)

**Framework**: AppKit  
**Kind**: init

Returns a representation of an image initialized with the specified PDF data.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(data pdfData: Data)
```

#### Return Value

An initialized [`NSPDFImageRep`](nspdfimagerep.md) object, or `nil` if the object could not be initialized. Initialization may fail if the PDF data does not conform to the PDF file format.

## Parameters

- `pdfData`: A data object containing the PDF data for the image.

## See Also

- [var pdfRepresentation: Data](nspdfimagerep/pdfrepresentation.md)
  The PDF representation of the representation’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspdfimagerep/init(data:))*