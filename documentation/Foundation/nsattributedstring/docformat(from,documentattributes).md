# docFormat(from:documentAttributes:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a data object that contains a Microsoft Word–format stream corresponding to the characters and attributes within the specified range.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func docFormat(from range: NSRange, documentAttributes dict: [NSAttributedString.DocumentAttributeKey : Any] = [:]) -> Data?
```

```objc
- (NSData *) docFormatFromRange:(NSRange) range documentAttributes:(NSDictionary<NSString *,id> *) dict;
```

#### Return Value

Returns a data object containing the attributed string as a Microsoft Word doc file.

#### Discussion

Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## Parameters

- `range`: The range.
- `dict`: A required dictionary specifying the document attributes. The dictionary contains values from `Document Types` and must at least contain [`documentType`](./documentattributekey/documenttype.md).

## See Also

### Exporting the string as data
- [func data(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) throws -> Data](./data%28from,documentattributes%29.md)
  Returns a data object that contains a text stream corresponding to the characters and attributes within the specified range.
- [func fileWrapper(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) throws -> FileWrapper](./filewrapper%28from,documentattributes%29.md)
  Returns a file wrapper object that contains a text stream corresponding to the characters and attributes within the specified range.
- [func rtf(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> Data?](./rtf%28from,documentattributes%29.md)
  Returns a data object that contains an RTF stream corresponding to the characters and attributes within the specified range, omitting all attachment attributes.
- [func rtfd(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> Data?](./rtfd%28from,documentattributes%29.md)
  Returns a data object that contains an RTFD stream corresponding to the characters and attributes within the specified range.
- [func rtfdFileWrapper(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> FileWrapper?](./rtfdfilewrapper%28from,documentattributes%29.md)
  Returns a file wrapper object that contains an RTFD document corresponding to the characters and attributes within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/docformat(from:documentattributes:))*