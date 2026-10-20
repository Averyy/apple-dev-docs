# filename

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

The file name of the MMS part.

**Availability**:
- iOS 26.0+

## Declaration

```swift
var filename: String
```

#### Discussion

If the file name is unavailable or doesn’t apply to this kind of content part, use an empty string.

## See Also

### Accessing part properties
- [var data: Data](./data.md)
  The raw data used for the MMS content part.
- [var disposition: MMSPartContent.MMSDispositionType](./disposition.md)
  The disposition of the MMS part, indicating whether the part renders inline or as an attachment.
- [MMSPartContent.MMSDispositionType](./mmsdispositiontype.md)
  A structure that defines the disposition of the content part when rendered.
- [var contentID: String](./contentid.md)
  A unique identifier for the part.
- [var contentType: UTType?](./contenttype.md)
  The content type of the part, as a Uniform Type Identifier.
- [struct UTType](../../UniformTypeIdentifiers/uttype-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmspartcontent/filename)*