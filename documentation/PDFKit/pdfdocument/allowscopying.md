# allowsCopying

**Framework**: PDFKit  
**Kind**: property

A Boolean value indicating whether the document allows copying of content to the Pasteboard.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var allowsCopying: Bool { get }
```

#### Discussion

The ability to copy content from a PDF document is an attribute unrelated to whether the document is locked or unlocked. It depends on the PDF permissions set by the document’s author.

This method only determines the desired permissions setting in the PDF document; it is up to the application to enforce (or ignore) the permissions.

This method always returns [`true`](https://developer.apple.com/documentation/Swift/true) if the document is not encrypted. Note that in many cases an encrypted document may still be readable by all users due to the standard empty string password. For more details about user and owner passwords, see the Adobe PDF specification.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/allowscopying)*