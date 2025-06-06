# rtfd(from:documentAttributes:)

**Framework**: Foundation  
**Kind**: method

Returns a data object that contains an RTFD stream corresponding to the characters and attributes within the specified range.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func rtfd(from range: NSRange, documentAttributes dict: [NSAttributedString.DocumentAttributeKey : Any] = [:]) -> Data?
```

#### Return Value

A data object containing the RTFD stream containing the characters and attributes.

#### Discussion

Writes the document-level attributes in `docAttributes`, as explained in [`RTF Files and Attributed Strings`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextAttributes/RTFAndAttrStrings.html#//apple_ref/doc/uid/20000164).

Raises an [`rangeException`](nsexceptionname/rangeexception.md) if any part of `aRange` lies beyond the end of the receiver’s characters.

When writing data to the pasteboard, you can use the `NSData` object as the first argument to the [`NSPasteboard`](https://developer.apple.com/documentation/AppKit/NSPasteboard) method [`setData(_:forType:)`](https://developer.apple.com/documentation/AppKit/NSPasteboard/setData(_:forType:)), with a second argument of `NSRTFPboardType`.

## Parameters

- `range`: The range.
- `dict`: A required dictionary specifying the document attributes. The dictionary contains values from   and must at least contain  .

## See Also

- [func data(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) throws -> Data](nsattributedstring/data(from:documentattributes:).md)
  Returns a data object that contains a text stream corresponding to the characters and attributes within the specified range.
- [func fileWrapper(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) throws -> FileWrapper](nsattributedstring/filewrapper(from:documentattributes:).md)
  Returns a file wrapper object that contains a text stream corresponding to the characters and attributes within the specified range.
- [func docFormat(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> Data?](nsattributedstring/docformat(from:documentattributes:).md)
  Returns a data object that contains a Microsoft Word–format stream corresponding to the characters and attributes within the specified range.
- [func rtf(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> Data?](nsattributedstring/rtf(from:documentattributes:).md)
  Returns a data object that contains an RTF stream corresponding to the characters and attributes within the specified range, omitting all attachment attributes.
- [func rtfdFileWrapper(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> FileWrapper?](nsattributedstring/rtfdfilewrapper(from:documentattributes:).md)
  Returns a file wrapper object that contains an RTFD document corresponding to the characters and attributes within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/rtfd(from:documentattributes:))*