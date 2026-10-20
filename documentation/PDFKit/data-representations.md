# Data Representations

**Framework**: PDFKit  
**Role**: API Collection

Operations to represent PDF documents as data objects.

## Topics

### Creating Data Representations
- [func dataRepresentation() -> Data?](./pdfdocument/datarepresentation%28%29.md)
  Returns a representation of the document as an `NSData` object.
- [func dataRepresentation(options: [AnyHashable : Any]) -> Data?](./pdfdocument/datarepresentation%28options%29.md)
  Returns a representation of the document as an `NSData` object with additional options applied, such as filters.

## See Also

### Writing Out the PDF Data
- [func write(toFile: String) -> Bool](./pdfdocument/write%28tofile%29.md)
  Writes the document to a file at the specified path.
- [func write(toFile: String, withOptions: [PDFDocumentWriteOption : Any]?) -> Bool](./pdfdocument/write%28tofile,withoptions%29.md)
  Writes the document to a file at the specified path with the specified options.
- [func write(to: URL) -> Bool](./pdfdocument/write%28to%29.md)
  Writes the document to a location specified by the passed-in URL.
- [func write(to: URL, withOptions: [PDFDocumentWriteOption : Any]?) -> Bool](./pdfdocument/write%28to,withoptions%29.md)
  Writes the document to the specified URL with the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/data-representations)*