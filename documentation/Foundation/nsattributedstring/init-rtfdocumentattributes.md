# init(RTF:documentAttributes:)

**Framework**: Foundation  
**Kind**: init

Creates an attributed string by decoding the stream of RTF commands and data in the specified data object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
init?(rtf data: Data, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

#### Return Value

Returns an initialized attributed string object, or `nil` if the method can’t decode the data.

#### Discussion

Also returns by reference in `dict` a dictionary containing document-level attributes described in [`NSAttributedString.DocumentAttributeKey`](nsattributedstring/documentattributekey.md). `dict` may be `NULL`, in which case no document attributes are returned. Returns an initialized object, or `nil` if `data` can’t be decoded.

## Parameters

- `data`: The data containing RTF content.
- `dict`: An in-out dictionary containing document-level attributes. On output, this method updates the dictionary to contain any document-specific keys found in the data. Specify   if you don’t want the document attributes.

## See Also

- [init?(RTFD: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(rtfd:documentattributes:).md)
  Creates an attributed string by decoding the stream of RTFD commands and data in the specified data object.
- [init?(RTFDFileWrapper: FileWrapper, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(rtfdfilewrapper:documentattributes:).md)
  Creates an attributed string from the specified file wrapper that contains an RTFD document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(rtf:documentattributes:))*