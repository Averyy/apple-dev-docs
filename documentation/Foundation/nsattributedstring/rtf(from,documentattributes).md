# rtf(from:documentAttributes:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a data object that contains an RTF stream corresponding to the characters and attributes within the specified range, omitting all attachment attributes.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func rtf(from range: NSRange, documentAttributes dict: [NSAttributedString.DocumentAttributeKey : Any] = [:]) -> Data?
```

```objc
- (NSData *) RTFFromRange:(NSRange) range documentAttributes:(NSDictionary<NSString *,id> *) dict;
```

## Return Value

A data object containing an RTF stream for the attributed string.

## Discussion

Writes the document-level attributes in `docAttributes`, as explained in [RTF Files and Attributed Strings](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextAttributes/RTFAndAttrStrings.html#//apple_ref/doc/uid/20000164).

Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if any part of `aRange` lies beyond the end of the receiver’s characters.

When writing data to the pasteboard, you can use the `NSData` object as the first argument to the [`NSPasteboard`](../../AppKit/nspasteboard.md) method [`setData(_:forType:)`](../../AppKit/nspasteboard/setdata%28_,fortype%29.md), with a second argument of `NSRTFPboardType`. Although this method strips attachments, it leaves the attachment characters in the text itself. The `NSText` method  [`rtf(from:)`](../../AppKit/nstext/rtf%28from%29.md), on the other hand, does strip attachment characters when extracting RTF.

## Parameters

- `range`: The range.
- `dict`: A required dictionary specifying the document attributes. The dictionary contains values from `Document Types` and must at least contain [`documentType`](./documentattributekey/documenttype.md).

## See Also

### Exporting the string as data
- [func data(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) throws -> Data](./data%28from,documentattributes%29.md)
  Returns a data object that contains a text stream corresponding to the characters and attributes within the specified range.
- [func fileWrapper(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) throws -> FileWrapper](./filewrapper%28from,documentattributes%29.md)
  Returns a file wrapper object that contains a text stream corresponding to the characters and attributes within the specified range.
- [func docFormat(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> Data?](./docformat%28from,documentattributes%29.md)
  Returns a data object that contains a Microsoft Word–format stream corresponding to the characters and attributes within the specified range.
- [func rtfd(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> Data?](./rtfd%28from,documentattributes%29.md)
  Returns a data object that contains an RTFD stream corresponding to the characters and attributes within the specified range.
- [func rtfdFileWrapper(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> FileWrapper?](./rtfdfilewrapper%28from,documentattributes%29.md)
  Returns a file wrapper object that contains an RTFD document corresponding to the characters and attributes within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/rtf(from:documentattributes:))*