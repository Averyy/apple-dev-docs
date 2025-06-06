# Permission Properties

**Framework**: PDFKit

Properties that specify what functions are allowed for a PDF document.

## Topics

### Getting Permissions
- [var allowsCopying: Bool](pdfdocument/allowscopying.md)
  A Boolean value indicating whether the document allows copying of content to the Pasteboard.
- [var allowsPrinting: Bool](pdfdocument/allowsprinting.md)
  A Boolean value indicating whether the document allows printing.
- [var allowsCommenting: Bool](pdfdocument/allowscommenting.md)
  A Boolean value indicating whether you can create or modify document annotations, including form field entries.
- [var allowsContentAccessibility: Bool](pdfdocument/allowscontentaccessibility.md)
  A Boolean value indicating whether you can extract content from the document, but only for the purpose of accessibility.
- [var allowsDocumentAssembly: Bool](pdfdocument/allowsdocumentassembly.md)
  A Boolean value indicating whether you can manage a document by inserting, deleting, and rotating pages.
- [var allowsDocumentChanges: Bool](pdfdocument/allowsdocumentchanges.md)
  A Boolean value indicating whether you can modify the document contents except for document attributes.
- [var allowsFormFieldEntry: Bool](pdfdocument/allowsformfieldentry.md)
  A Boolean value indicating whether you can modify form field entries even if you can’t edit document annotations.

## See Also

- [var isEncrypted: Bool](pdfdocument/isencrypted.md)
  A Boolean value specifying whether the document is encrypted.
- [var isLocked: Bool](pdfdocument/islocked.md)
  A Boolean value indicating whether the document is locked.
- [func unlock(withPassword: String) -> Bool](pdfdocument/unlock(withpassword:).md)
  Attempts to unlock an encrypted document.
- [var permissionsStatus: PDFDocumentPermissions](pdfdocument/permissionsstatus.md)
  The permissions status of the PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/permission-properties)*