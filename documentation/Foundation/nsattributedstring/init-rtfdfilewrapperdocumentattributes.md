# init(RTFDFileWrapper:documentAttributes:)

**Framework**: Foundation  
**Kind**: init

Creates an attributed string from the specified file wrapper that contains an RTFD document.

**Availability**:
- macOS 10.0+

## Declaration

```swift
init?(rtfdFileWrapper wrapper: FileWrapper, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

#### Return Value

Returns an initialized attributed string object, or `nil` if the method can’t decode the data.

#### Discussion

Also returns by reference in `dict` a dictionary containing document-level attributes described in [`NSAttributedString.DocumentAttributeKey`](nsattributedstring/documentattributekey.md). `dict` may be `NULL`, in which case no document attributes are returned. Returns an initialized object, or `nil` if `wrapper` can’t be interpreted as an RTFD document.

## Parameters

- `wrapper`: The   containing the RTFD document.
- `dict`: An in-out dictionary containing document-level attributes. On output, this method updates the dictionary to contain any document-specific keys found in the data. Specify   if you don’t want the document attributes.

## See Also

- [init?(RTF: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(rtf:documentattributes:).md)
  Creates an attributed string by decoding the stream of RTF commands and data in the specified data object.
- [init?(RTFD: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](nsattributedstring/init(rtfd:documentattributes:).md)
  Creates an attributed string by decoding the stream of RTFD commands and data in the specified data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(rtfdfilewrapper:documentattributes:))*