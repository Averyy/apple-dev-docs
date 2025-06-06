# string

**Framework**: PDFKit  
**Kind**: property

A string representing the textual content for the entire document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var string: String? { get }
```

#### Return Value

A string that represents the textual content of the entire document.

#### Discussion

Pages are delimited with linefeed characters.

This is a convenience method, equivalent to creating a selection object for the entire document and then invoking the `PDFSelection` class’s [`string`](pdfselection/string.md) method.

## See Also

- [var documentURL: URL?](pdfdocument/documenturl.md)
  The URL for the document.
- [var majorVersion: Int](pdfdocument/majorversion.md)
  The major version of the document.
- [var minorVersion: Int](pdfdocument/minorversion.md)
  The minor version of the document.
- [func outlineItem(for: PDFSelection) -> PDFOutline?](pdfdocument/outlineitem(for:).md)
  Returns the most likely parent PDF outline object for the selection.
- [var outlineRoot: PDFOutline?](pdfdocument/outlineroot.md)
  The document’s root outline to a PDF outline object.
- [var documentAttributes: [AnyHashable : Any]?](pdfdocument/documentattributes.md)
  A dictionary of document metadata.
- [var documentRef: CGPDFDocument?](pdfdocument/documentref.md)
  The `CGPDFDocument` associated with the `PDFDocument` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/string)*