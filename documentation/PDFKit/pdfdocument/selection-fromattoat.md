# selection(from:at:to:at:)

**Framework**: PDFKit  
**Kind**: method

Returns the specified selection based on starting and ending points.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func selection(from startPage: PDFPage, at startPoint: NSPoint, to endPage: PDFPage, at endPoint: NSPoint) -> PDFSelection?
```

#### Discussion

The selection begins at `startPt` on `startPage` and ends at `endPt` on `endPage`. The starting and ending points should be specified in page space, relative to their respective pages.

The starting and ending points can be on the same page. In this case, invoking this method is equivalent to sending the `selectionFromPoint:toPoint:` message to a `PDFPage` object.

Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page.

## See Also

- [func selection(for: NSRange) -> PDFSelection?](pdfpage/selection(for:)-20y9d.md)
  Returns the text contained within the specified range.
- [func selection(from: PDFPage, atCharacterIndex: Int, to: PDFPage, atCharacterIndex: Int) -> PDFSelection?](pdfdocument/selection(from:atcharacterindex:to:atcharacterindex:).md)
  Returns the specified selection based on starting and ending character indexes.
- [var selectionForEntireDocument: PDFSelection?](pdfdocument/selectionforentiredocument.md)
  Returns a selection representing the textual content of the entire document.
- [Search Operations](search-operations.md)
  Find and search in PDFs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/selection(from:at:to:at:))*