# MMSPartContent.MMSDispositionType

**Framework**: TelephonyMessagingKit  
**Kind**: enum  
**Role**: Enumeration

A structure that defines the disposition of the content part when rendered.

**Availability**:
- iOS 26.0+

## Declaration

```swift
enum MMSDispositionType
```

## Topics

### Working with disposition types
- [MMSPartContent.MMSDispositionType.attachment](./mmsdispositiontype/attachment.md)
  A disposition to render the content part as an attachment to the message.
- [MMSPartContent.MMSDispositionType.inline](./mmsdispositiontype/inline.md)
  A disposition to render the content part in line with the rest of the message.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing part properties
- [var data: Data](./data.md)
  The raw data used for the MMS content part.
- [var disposition: MMSPartContent.MMSDispositionType](./disposition.md)
  The disposition of the MMS part, indicating whether the part renders inline or as an attachment.
- [var filename: String](./filename.md)
  The file name of the MMS part.
- [var contentID: String](./contentid.md)
  A unique identifier for the part.
- [var contentType: UTType?](./contenttype.md)
  The content type of the part, as a Uniform Type Identifier.
- [struct UTType](../../UniformTypeIdentifiers/uttype-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmspartcontent/mmsdispositiontype)*