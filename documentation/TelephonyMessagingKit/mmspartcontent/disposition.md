# disposition

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

The disposition of the MMS part, indicating whether the part renders inline or as an attachment.

**Availability**:
- iOS 26.0+

## Declaration

```swift
var disposition: MMSPartContent.MMSDispositionType
```

## See Also

### Accessing part properties
- [var data: Data](./data.md)
  The raw data used for the MMS content part.
- [MMSPartContent.MMSDispositionType](./mmsdispositiontype.md)
  A structure that defines the disposition of the content part when rendered.
- [var filename: String](./filename.md)
  The file name of the MMS part.
- [var contentID: String](./contentid.md)
  A unique identifier for the part.
- [var contentType: UTType?](./contenttype.md)
  The content type of the part, as a Uniform Type Identifier.
- [struct UTType](../../UniformTypeIdentifiers/uttype-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmspartcontent/disposition)*