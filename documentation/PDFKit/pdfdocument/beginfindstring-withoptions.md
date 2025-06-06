# beginFindString(_:withOptions:)

**Framework**: PDFKit  
**Kind**: method

Asynchronously finds all instances of the specified string in the document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func beginFindString(_ string: String, withOptions options: NSString.CompareOptions = [])
```

#### Discussion

This method returns immediately. It causes notifications to be issued when searching begins and ends, on each search hit, and when the search proceeds to a new page. For options, refer to [`Searching, Comparing, and Sorting Strings`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/SearchingStrings.html#//apple_ref/doc/uid/20000149).

## See Also

- [func findString(String, withOptions: NSString.CompareOptions) -> [PDFSelection]](pdfdocument/findstring(_:withoptions:).md)
  Synchronously finds all instances of the specified string in the document.
- [func beginFindStrings([String], withOptions: NSString.CompareOptions)](pdfdocument/beginfindstrings(_:withoptions:).md)
  Asynchronously finds all instances of the specified array of strings in the document.
- [func findString(String, fromSelection: PDFSelection?, withOptions: NSString.CompareOptions) -> PDFSelection?](pdfdocument/findstring(_:fromselection:withoptions:).md)
  Synchronously finds the next occurance of a string after the specified selection (or before the selection if you specified `NSBackwardsSearch` as a search option.
- [var isFinding: Bool](pdfdocument/isfinding.md)
  Returns a Boolean value indicating whether an asynchronous find operation is in progress.
- [func cancelFindString()](pdfdocument/cancelfindstring.md)
  Cancels a search initiated with [`beginFindString(_:withOptions:)`](pdfdocument/beginfindstring(_:withoptions:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/beginfindstring(_:withoptions:))*