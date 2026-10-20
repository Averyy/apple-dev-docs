# Search Operations

**Framework**: PDFKit  
**Role**: API Collection

Find and search in PDFs.

## Topics

### Searching Documents
- [func findString(String, withOptions: NSString.CompareOptions) -> [PDFSelection]](./pdfdocument/findstring%28_,withoptions%29.md)
  Synchronously finds all instances of the specified string in the document.
- [func beginFindString(String, withOptions: NSString.CompareOptions)](./pdfdocument/beginfindstring%28_,withoptions%29.md)
  Asynchronously finds all instances of the specified string in the document.
- [func beginFindStrings([String], withOptions: NSString.CompareOptions)](./pdfdocument/beginfindstrings%28_,withoptions%29.md)
  Asynchronously finds all instances of the specified array of strings in the document.
- [func findString(String, fromSelection: PDFSelection?, withOptions: NSString.CompareOptions) -> PDFSelection?](./pdfdocument/findstring%28_,fromselection,withoptions%29.md)
  Synchronously finds the next occurance of a string after the specified selection (or before the selection if you specified `NSBackwardsSearch` as a search option.
- [var isFinding: Bool](./pdfdocument/isfinding.md)
  Returns a Boolean value indicating whether an asynchronous find operation is in progress.
- [func cancelFindString()](./pdfdocument/cancelfindstring%28%29.md)
  Cancels a search initiated with [`beginFindString(_:withOptions:)`](./pdfdocument/beginfindstring%28_,withoptions%29.md).

## See Also

### Working with Selections and Searches
- [func selection(from: PDFPage, atCharacterIndex: Int, to: PDFPage, atCharacterIndex: Int) -> PDFSelection?](./pdfdocument/selection%28from,atcharacterindex,to,atcharacterindex%29.md)
  Returns the specified selection based on starting and ending character indexes.
- [func selection(from: PDFPage, at: CGPoint, to: PDFPage, at: CGPoint) -> PDFSelection?](./pdfdocument/selection%28from,at,to,at%29.md)
  Returns the specified selection based on starting and ending points.
- [var selectionForEntireDocument: PDFSelection?](./pdfdocument/selectionforentiredocument.md)
  Returns a selection representing the textual content of the entire document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/search-operations)*