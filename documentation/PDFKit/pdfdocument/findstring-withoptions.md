# findString(_:withOptions:)

**Framework**: PDFKit  
**Kind**: method

Synchronously finds all instances of the specified string in the document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func findString(_ string: String, withOptions options: NSString.CompareOptions = []) -> [PDFSelection]
```

#### Discussion

Each hit gets added to an `NSArray` object as a [`PDFSelection`](pdfselection.md) object. If there are no hits, this method returns an empty array.

Use this method when the complete search process will be brief and when you don’t need the flexibility or control offered by [`beginFindString(_:withOptions:)`](pdfdocument/beginfindstring(_:withoptions:).md). For options, refer to [`Searching, Comparing, and Sorting Strings`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/SearchingStrings.html#//apple_ref/doc/uid/20000149).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/findstring(_:withoptions:))*