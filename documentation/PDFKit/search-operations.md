# Search Operations

**Framework**: PDFKit

Find and search in PDFs.

## Topics

### Searching Documents
- [func findString(String, withOptions: NSString.CompareOptions) -> [PDFSelection]](pdfdocument/findstring(_:withoptions:).md)
  Synchronously finds all instances of the specified string in the document.
- [func beginFindString(String, withOptions: NSString.CompareOptions)](pdfdocument/beginfindstring(_:withoptions:).md)
  Asynchronously finds all instances of the specified string in the document.
- [func beginFindStrings([String], withOptions: NSString.CompareOptions)](pdfdocument/beginfindstrings(_:withoptions:).md)
  Asynchronously finds all instances of the specified array of strings in the document.
- [func findString(String, fromSelection: PDFSelection?, withOptions: NSString.CompareOptions) -> PDFSelection?](pdfdocument/findstring(_:fromselection:withoptions:).md)
  Synchronously finds the next occurance of a string after the specified selection (or before the selection if you specified `NSBackwardsSearch` as a search option.
- [var isFinding: Bool](pdfdocument/isfinding.md)
  Returns a Boolean value indicating whether an asynchronous find operation is in progress.
- [func cancelFindString()](pdfdocument/cancelfindstring.md)
  Cancels a search initiated with [`beginFindString(_:withOptions:)`](pdfdocument/beginfindstring(_:withoptions:).md).

## See Also

- [func selection(from: PDFPage, atCharacterIndex: Int, to: PDFPage, atCharacterIndex: Int) -> PDFSelection?](pdfdocument/selection(from:atcharacterindex:to:atcharacterindex:).md)
  Returns the specified selection based on starting and ending character indexes.
- [func selection(from: PDFPage, at: CGPoint, to: PDFPage, at: CGPoint) -> PDFSelection?](pdfdocument/selection(from:at:to:at:).md)
  Returns the specified selection based on starting and ending points.
- [var selectionForEntireDocument: PDFSelection?](pdfdocument/selectionforentiredocument.md)
  Returns a selection representing the textual content of the entire document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/search-operations)*