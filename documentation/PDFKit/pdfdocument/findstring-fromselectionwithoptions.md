# findString(_:fromSelection:withOptions:)

**Framework**: PDFKit  
**Kind**: method

Synchronously finds the next occurance of a string after the specified selection (or before the selection if you specified `NSBackwardsSearch` as a search option.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func findString(_ string: String, fromSelection selection: PDFSelection?, withOptions options: NSString.CompareOptions = []) -> PDFSelection?
```

#### Discussion

Matches are returned as a [`PDFSelection`](pdfselection.md) object. If the search reaches the end (or beginning) of the document without any hits, this method returns `NULL`.

If you pass `NULL` for the selection, this method begins searching from the beginning of the document (or the end, if you specified `NSBackwardsSearch`).

You can use this method to implement “Find Again” behavior. For options, refer to [`Searching, Comparing, and Sorting Strings`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/SearchingStrings.html#//apple_ref/doc/uid/20000149).

## See Also

- [func findString(String, withOptions: NSString.CompareOptions) -> [PDFSelection]](pdfdocument/findstring(_:withoptions:).md)
  Synchronously finds all instances of the specified string in the document.
- [func beginFindString(String, withOptions: NSString.CompareOptions)](pdfdocument/beginfindstring(_:withoptions:).md)
  Asynchronously finds all instances of the specified string in the document.
- [func beginFindStrings([String], withOptions: NSString.CompareOptions)](pdfdocument/beginfindstrings(_:withoptions:).md)
  Asynchronously finds all instances of the specified array of strings in the document.
- [var isFinding: Bool](pdfdocument/isfinding.md)
  Returns a Boolean value indicating whether an asynchronous find operation is in progress.
- [func cancelFindString()](pdfdocument/cancelfindstring.md)
  Cancels a search initiated with [`beginFindString(_:withOptions:)`](pdfdocument/beginfindstring(_:withoptions:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/findstring(_:fromselection:withoptions:))*