# docFormat(from:documentAttributes:)

**Framework**: Foundation  
**Kind**: method

Returns a data object that contains a Microsoft Word–format stream corresponding to the characters and attributes within the specified range.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func docFormat(from range: NSRange, documentAttributes dict: [NSAttributedString.DocumentAttributeKey : Any] = [:]) -> Data?
```

#### Return Value

Returns a data object containing the attributed string as a Microsoft Word doc file.

#### Discussion

Raises an [`rangeException`](nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## Parameters

- `range`: The range.
- `dict`: A required dictionary specifying the document attributes. The dictionary contains values from   and must at least contain  .

## See Also

- [func data(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) throws -> Data](nsattributedstring/data(from:documentattributes:).md)
  Returns a data object that contains a text stream corresponding to the characters and attributes within the specified range.
- [func fileWrapper(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) throws -> FileWrapper](nsattributedstring/filewrapper(from:documentattributes:).md)
  Returns a file wrapper object that contains a text stream corresponding to the characters and attributes within the specified range.
- [func rtf(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> Data?](nsattributedstring/rtf(from:documentattributes:).md)
  Returns a data object that contains an RTF stream corresponding to the characters and attributes within the specified range, omitting all attachment attributes.
- [func rtfd(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> Data?](nsattributedstring/rtfd(from:documentattributes:).md)
  Returns a data object that contains an RTFD stream corresponding to the characters and attributes within the specified range.
- [func rtfdFileWrapper(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> FileWrapper?](nsattributedstring/rtfdfilewrapper(from:documentattributes:).md)
  Returns a file wrapper object that contains an RTFD document corresponding to the characters and attributes within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/docformat(from:documentattributes:))*