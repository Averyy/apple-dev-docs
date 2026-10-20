# Write Operations

**Framework**: PDFKit  
**Role**: API Collection

Operations that let you write document data to different locations.

## Topics

### Writing Out the PDF Data
- [func write(toFile: String) -> Bool](./pdfdocument/write%28tofile%29.md)
  Writes the document to a file at the specified path.
- [func write(toFile: String, withOptions: [PDFDocumentWriteOption : Any]?) -> Bool](./pdfdocument/write%28tofile,withoptions%29.md)
  Writes the document to a file at the specified path with the specified options.
- [func write(to: URL) -> Bool](./pdfdocument/write%28to%29.md)
  Writes the document to a location specified by the passed-in URL.
- [func write(to: URL, withOptions: [PDFDocumentWriteOption : Any]?) -> Bool](./pdfdocument/write%28to,withoptions%29.md)
  Writes the document to the specified URL with the specified options.
- [Data Representations](./data-representations.md)
  Operations to represent PDF documents as data objects.
### Printing Documents for macOS
- [func printOperation(for: NSPrintInfo?, scalingMode: PDFPrintScalingMode, autoRotate: Bool) -> NSPrintOperation?](./pdfdocument/printoperation%28for,scalingmode,autorotate%29.md)
  Returns a print operation suitable for printing the PDF document.
- [enum PDFPrintScalingMode](./pdfprintscalingmode.md)
  The type of scaling to be used when printing a page (see [`PDFDocument`](./pdfdocument.md)).

## See Also

### Reading and Writing PDFs
- [Read Operations](./read-operations.md)
  Operations that let you access documents and pages, manage document security, and work with searching and selections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/write-operations)*