# beginFindStrings(_:withOptions:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Asynchronously finds all instances of the specified array of strings in the document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func beginFindStrings(_ strings: [String], withOptions options: NSString.CompareOptions = [])
```

```objc
- (void) beginFindStrings:(NSArray<NSString *> *) strings withOptions:(NSStringCompareOptions) options;
```

#### Discussion

This method returns immediately. It causes notifications to be issued when searching begins and ends, on each search hit, and when the search proceeds to a new page. For options, refer to [Searching, Comparing, and Sorting Strings](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/SearchingStrings.html#//apple_ref/doc/uid/20000149).

## See Also

### Related Documentation
- [class PDFDocument](../pdfdocument.md)
  An object that represents PDF data or a PDF file and defines methods for writing, searching, and selecting PDF data.
### Searching Documents
- [func findString(String, withOptions: NSString.CompareOptions) -> [PDFSelection]](./findstring%28_,withoptions%29.md)
  Synchronously finds all instances of the specified string in the document.
- [func beginFindString(String, withOptions: NSString.CompareOptions)](./beginfindstring%28_,withoptions%29.md)
  Asynchronously finds all instances of the specified string in the document.
- [func findString(String, fromSelection: PDFSelection?, withOptions: NSString.CompareOptions) -> PDFSelection?](./findstring%28_,fromselection,withoptions%29.md)
  Synchronously finds the next occurance of a string after the specified selection (or before the selection if you specified `NSBackwardsSearch` as a search option.
- [var isFinding: Bool](./isfinding.md)
  Returns a Boolean value indicating whether an asynchronous find operation is in progress.
- [func cancelFindString()](./cancelfindstring%28%29.md)
  Cancels a search initiated with [`beginFindString(_:withOptions:)`](./beginfindstring%28_,withoptions%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/beginfindstrings(_:withoptions:))*