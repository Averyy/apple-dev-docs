# selectionForEntireDocument

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) PDFSelection * selectionForEntireDocument;
```

## See Also

### Working with Selections and Searches
- [func selection(from: PDFPage, atCharacterIndex: Int, to: PDFPage, atCharacterIndex: Int) -> PDFSelection?](./selection%28from,atcharacterindex,to,atcharacterindex%29.md)
  Returns the specified selection based on starting and ending character indexes.
- [func selection(from: PDFPage, at: CGPoint, to: PDFPage, at: CGPoint) -> PDFSelection?](./selection%28from,at,to,at%29.md)
  Returns the specified selection based on starting and ending points.
- [Search Operations](../search-operations.md)
  Find and search in PDFs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/selectionforentiredocument)*