# selectionForEntireDocument

**Framework**: PDFKit  
**Kind**: property

Returns a selection representing the textual content of the entire document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var selectionForEntireDocument: PDFSelection? { get }
```

## See Also

- [func selection(from: PDFPage, atCharacterIndex: Int, to: PDFPage, atCharacterIndex: Int) -> PDFSelection?](pdfdocument/selection(from:atcharacterindex:to:atcharacterindex:).md)
  Returns the specified selection based on starting and ending character indexes.
- [func selection(from: PDFPage, at: CGPoint, to: PDFPage, at: CGPoint) -> PDFSelection?](pdfdocument/selection(from:at:to:at:).md)
  Returns the specified selection based on starting and ending points.
- [Search Operations](search-operations.md)
  Find and search in PDFs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/selectionforentiredocument)*