# Data Representations

**Framework**: PDFKit

Operations to represent PDF documents as data objects.

## Topics

### Creating Data Representations
- [func dataRepresentation() -> Data?](pdfdocument/datarepresentation.md)
  Returns a representation of the document as an `NSData` object.
- [func dataRepresentation(options: [AnyHashable : Any]) -> Data?](pdfdocument/datarepresentation(options:).md)
  Returns a representation of the document as an `NSData` object with additional options applied, such as filters.

## See Also

- [func write(toFile: String) -> Bool](pdfdocument/write(tofile:).md)
  Writes the document to a file at the specified path.
- [func write(toFile: String, withOptions: [PDFDocumentWriteOption : Any]?) -> Bool](pdfdocument/write(tofile:withoptions:).md)
  Writes the document to a file at the specified path with the specified options.
- [func write(to: URL) -> Bool](pdfdocument/write(to:).md)
  Writes the document to a location specified by the passed-in URL.
- [func write(to: URL, withOptions: [PDFDocumentWriteOption : Any]?) -> Bool](pdfdocument/write(to:withoptions:).md)
  Writes the document to the specified URL with the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/data-representations)*