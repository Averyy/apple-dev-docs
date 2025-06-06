# outlineRoot

**Framework**: PDFKit  
**Kind**: property

The document’s root outline to a PDF outline object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var outlineRoot: PDFOutline? { get set }
```

#### Discussion

When a PDF document is saved, the outline tree structure is written out to the destination PDF file.

## Parameters

- `outline`: The outline to be used as the document’s root outline. Pass   to strip the outline from a document.

## See Also

- [class PDFDocument](pdfdocument.md)
  An object that represents PDF data or a PDF file and defines methods for writing, searching, and selecting PDF data.
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
- [var documentAttributes: [AnyHashable : Any]?](pdfdocument/documentattributes.md)
  A dictionary of document metadata.
- [var documentRef: CGPDFDocument?](pdfdocument/documentref.md)
  The `CGPDFDocument` associated with the `PDFDocument` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/outlineroot)*