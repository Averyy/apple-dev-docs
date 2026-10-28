# selection(from:atCharacterIndex:to:atCharacterIndex:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns the specified selection based on starting and ending character indexes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func selection(from startPage: PDFPage, atCharacterIndex startCharacter: Int, to endPage: PDFPage, atCharacterIndex endCharacter: Int) -> PDFSelection?
```

```objc
- (PDFSelection *) selectionFromPage:(PDFPage *) startPage atCharacterIndex:(NSUInteger) startCharacter toPage:(PDFPage *) endPage atCharacterIndex:(NSUInteger) endCharacter;
```

## Discussion

The selection begins at `startChar` on `startPage` and ends at `endChar` on `endPage`. The starting and ending index values must be in the range of the number of characters (as returned by [`numberOfCharacters`](../pdfpage/numberofcharacters.md)) within the respective `PDFPage` objects.

## See Also

### Working with Selections and Searches
- [func selection(from: PDFPage, at: CGPoint, to: PDFPage, at: CGPoint) -> PDFSelection?](./selection%28from,at,to,at%29.md)
  Returns the specified selection based on starting and ending points.
- [var selectionForEntireDocument: PDFSelection?](./selectionforentiredocument.md)
  Returns a selection representing the textual content of the entire document.
- [Search Operations](../search-operations.md)
  Find and search in PDFs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/selection(from:atcharacterindex:to:atcharacterindex:))*