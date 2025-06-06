# Read Operations

**Framework**: PDFKit

Operations that let you access documents and pages, manage document security, and work with searching and selections.

## Topics

### Accessing Document Information
- [var documentURL: URL?](pdfdocument/documenturl.md)
  The URL for the document.
- [var majorVersion: Int](pdfdocument/majorversion.md)
  The major version of the document.
- [var minorVersion: Int](pdfdocument/minorversion.md)
  The minor version of the document.
- [var string: String?](pdfdocument/string.md)
  A string representing the textual content for the entire document.
- [func outlineItem(for: PDFSelection) -> PDFOutline?](pdfdocument/outlineitem(for:).md)
  Returns the most likely parent PDF outline object for the selection.
- [var outlineRoot: PDFOutline?](pdfdocument/outlineroot.md)
  The document’s root outline to a PDF outline object.
- [var documentAttributes: [AnyHashable : Any]?](pdfdocument/documentattributes.md)
  A dictionary of document metadata.
- [var documentRef: CGPDFDocument?](pdfdocument/documentref.md)
  The `CGPDFDocument` associated with the `PDFDocument` object.
### Managing Document Security
- [var isEncrypted: Bool](pdfdocument/isencrypted.md)
  A Boolean value specifying whether the document is encrypted.
- [var isLocked: Bool](pdfdocument/islocked.md)
  A Boolean value indicating whether the document is locked.
- [func unlock(withPassword: String) -> Bool](pdfdocument/unlock(withpassword:).md)
  Attempts to unlock an encrypted document.
- [var permissionsStatus: PDFDocumentPermissions](pdfdocument/permissionsstatus.md)
  The permissions status of the PDF document.
- [Permission Properties](permission-properties.md)
  Properties that specify what functions are allowed for a PDF document.
### Working with Selections and Searches
- [func selection(from: PDFPage, atCharacterIndex: Int, to: PDFPage, atCharacterIndex: Int) -> PDFSelection?](pdfdocument/selection(from:atcharacterindex:to:atcharacterindex:).md)
  Returns the specified selection based on starting and ending character indexes.
- [func selection(from: PDFPage, at: CGPoint, to: PDFPage, at: CGPoint) -> PDFSelection?](pdfdocument/selection(from:at:to:at:).md)
  Returns the specified selection based on starting and ending points.
- [var selectionForEntireDocument: PDFSelection?](pdfdocument/selectionforentiredocument.md)
  Returns a selection representing the textual content of the entire document.
- [Search Operations](search-operations.md)
  Find and search in PDFs.
### Working with Pages
- [var pageCount: Int](pdfdocument/pagecount.md)
  The number of pages in the document.
- [func page(at: Int) -> PDFPage?](pdfdocument/page(at:).md)
  Returns the page at the specified index number.
- [func index(for: PDFPage) -> Int](pdfdocument/index(for:).md)
  Gets the index number for the specified page.
- [func insert(PDFPage, at: Int)](pdfdocument/insert(_:at:).md)
  Inserts a page at the specified index point.
- [func removePage(at: Int)](pdfdocument/removepage(at:).md)
  Removes the page at the specified index point.
- [func exchangePage(at: Int, withPageAt: Int)](pdfdocument/exchangepage(at:withpageat:).md)
  Swaps one page with another.
- [var pageClass: AnyClass](pdfdocument/pageclass.md)
  The class that is allocated and initialized when page objects are created for the document.

## See Also

- [Write Operations](write-operations.md)
  Operations that let you write document data to different locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/read-operations)*