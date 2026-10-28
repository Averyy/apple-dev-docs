# rtfdFileWrapper(from:documentAttributes:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a file wrapper object that contains an RTFD document corresponding to the characters and attributes within the specified range.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func rtfdFileWrapper(from range: NSRange, documentAttributes dict: [NSAttributedString.DocumentAttributeKey : Any] = [:]) -> FileWrapper?
```

```objc
- (NSFileWrapper *) RTFDFileWrapperFromRange:(NSRange) range documentAttributes:(NSDictionary<NSString *,id> *) dict;
```

## Return Value

A file wrapper containing the RTFD data.

## Discussion

The file wrapper also includes the document-level attributes in `docAttributes`, as explained in [RTF Files and Attributed Strings](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextAttributes/RTFAndAttrStrings.html#//apple_ref/doc/uid/20000164).

Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if any part of `aRange` lies beyond the end of the receiver’s characters.

You can save the file wrapper using the [`write(toFile:atomically:updateFilenames:)`](../filewrapper/write%28tofile,atomically,updatefilenames%29.md) method of [`FileWrapper`](../filewrapper.md).

## Parameters

- `range`: The range.
- `dict`: A required dictionary specifying the document attributes. The dictionary contains values from `Document Types` and must at least contain `NSDocumentTypeDocumentAttribute`.

## See Also

### Exporting the string as data
- [func data(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) throws -> Data](./data%28from,documentattributes%29.md)
  Returns a data object that contains a text stream corresponding to the characters and attributes within the specified range.
- [func fileWrapper(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) throws -> FileWrapper](./filewrapper%28from,documentattributes%29.md)
  Returns a file wrapper object that contains a text stream corresponding to the characters and attributes within the specified range.
- [func docFormat(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> Data?](./docformat%28from,documentattributes%29.md)
  Returns a data object that contains a Microsoft Word–format stream corresponding to the characters and attributes within the specified range.
- [func rtf(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> Data?](./rtf%28from,documentattributes%29.md)
  Returns a data object that contains an RTF stream corresponding to the characters and attributes within the specified range, omitting all attachment attributes.
- [func rtfd(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> Data?](./rtfd%28from,documentattributes%29.md)
  Returns a data object that contains an RTFD stream corresponding to the characters and attributes within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/rtfdfilewrapper(from:documentattributes:))*