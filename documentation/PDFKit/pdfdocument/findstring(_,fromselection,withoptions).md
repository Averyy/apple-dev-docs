# findString(_:fromSelection:withOptions:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (PDFSelection *) findString:(NSString *) string fromSelection:(PDFSelection *) selection withOptions:(NSStringCompareOptions) options;
```

## Discussion

Matches are returned as a [`PDFSelection`](../pdfselection.md) object. If the search reaches the end (or beginning) of the document without any hits, this method returns `NULL`.

If you pass `NULL` for the selection, this method begins searching from the beginning of the document (or the end, if you specified `NSBackwardsSearch`).

You can use this method to implement “Find Again” behavior. For options, refer to [Searching, Comparing, and Sorting Strings](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/SearchingStrings.html#//apple_ref/doc/uid/20000149).

## See Also

### Searching Documents
- [func findString(String, withOptions: NSString.CompareOptions) -> [PDFSelection]](./findstring%28_,withoptions%29.md)
  Synchronously finds all instances of the specified string in the document.
- [func beginFindString(String, withOptions: NSString.CompareOptions)](./beginfindstring%28_,withoptions%29.md)
  Asynchronously finds all instances of the specified string in the document.
- [func beginFindStrings([String], withOptions: NSString.CompareOptions)](./beginfindstrings%28_,withoptions%29.md)
  Asynchronously finds all instances of the specified array of strings in the document.
- [var isFinding: Bool](./isfinding.md)
  Returns a Boolean value indicating whether an asynchronous find operation is in progress.
- [func cancelFindString()](./cancelfindstring%28%29.md)
  Cancels a search initiated with [`beginFindString(_:withOptions:)`](./beginfindstring%28_,withoptions%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/findstring(_:fromselection:withoptions:))*