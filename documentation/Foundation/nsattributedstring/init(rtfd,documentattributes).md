# init(RTFD:documentAttributes:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates an attributed string by decoding the stream of RTFD commands and data in the specified data object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
init?(RTFD data: Data, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

```swift
init?(rtfd data: Data, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

```objc
- (instancetype) initWithRTFD:(NSData *) data documentAttributes:(NSDictionary<NSString *,id> **) dict;
```

## Return Value

Returns an initialized attributed string object, or `nil` if the method can’t decode the data.

## Parameters

- `data`: The data containing the RTFD content.
- `dict`: An in-out dictionary containing document-level attributes. On output, this method updates the dictionary to contain any document-specific keys found in the data. Specify `nil` if you don’t want the document attributes.

## See Also

### Creating from RTF
- [init?(RTF: Data, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./init%28rtf,documentattributes%29.md)
  Creates an attributed string by decoding the stream of RTF commands and data in the specified data object.
- [init?(RTFDFileWrapper: FileWrapper, documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./init%28rtfdfilewrapper,documentattributes%29.md)
  Creates an attributed string from the specified file wrapper that contains an RTFD document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(rtfd:documentattributes:))*