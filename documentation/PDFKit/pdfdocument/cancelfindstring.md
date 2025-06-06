# cancelFindString()

**Framework**: PDFKit  
**Kind**: method

Cancels a search initiated with [`beginFindString(_:withOptions:)`](pdfdocument/beginfindstring(_:withoptions:).md).

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func cancelFindString()
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/cancelfindstring())*