# documentURL

**Framework**: PDFKit  
**Kind**: property

The URL for the document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var documentURL: URL? { get }
```

#### Return Value

The URL for the document; may return `NULL` if the document was created from an `NSData` object.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/documenturl)*