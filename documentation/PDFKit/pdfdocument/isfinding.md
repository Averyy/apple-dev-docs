# isFinding

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value indicating whether an asynchronous find operation is in progress.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isFinding: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isFinding;
```

## See Also

### Searching Documents
- [func findString(String, withOptions: NSString.CompareOptions) -> [PDFSelection]](./findstring%28_,withoptions%29.md)
  Synchronously finds all instances of the specified string in the document.
- [func beginFindString(String, withOptions: NSString.CompareOptions)](./beginfindstring%28_,withoptions%29.md)
  Asynchronously finds all instances of the specified string in the document.
- [func beginFindStrings([String], withOptions: NSString.CompareOptions)](./beginfindstrings%28_,withoptions%29.md)
  Asynchronously finds all instances of the specified array of strings in the document.
- [func findString(String, fromSelection: PDFSelection?, withOptions: NSString.CompareOptions) -> PDFSelection?](./findstring%28_,fromselection,withoptions%29.md)
  Synchronously finds the next occurance of a string after the specified selection (or before the selection if you specified `NSBackwardsSearch` as a search option.
- [func cancelFindString()](./cancelfindstring%28%29.md)
  Cancels a search initiated with [`beginFindString(_:withOptions:)`](./beginfindstring%28_,withoptions%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/isfinding)*