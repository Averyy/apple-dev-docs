# MMSPartContent.MMSDispositionType

**Framework**: TelephonyMessagingKit  
**Kind**: enum

A structure that defines the disposition of the content part when rendered.

**Availability**:
- iOS 26.0+

## Declaration

```swift
enum MMSDispositionType
```

## Topics

### Working with disposition types
- [MMSPartContent.MMSDispositionType.attachment](mmspartcontent/mmsdispositiontype/attachment.md)
  A disposition to render the content part as an attachment to the message.
- [MMSPartContent.MMSDispositionType.inline](mmspartcontent/mmsdispositiontype/inline.md)
  A disposition to render the content part in line with the rest of the message.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var data: Data](mmspartcontent/data.md)
  The raw data used for the MMS content part.
- [var disposition: MMSPartContent.MMSDispositionType](mmspartcontent/disposition.md)
  The disposition of the MMS part, indicating whether the part renders inline or as an attachment.
- [var filename: String](mmspartcontent/filename.md)
  The file name of the MMS part.
- [var contentID: String](mmspartcontent/contentid.md)
  A unique identifier for the part.
- [var contentType: UTType?](mmspartcontent/contenttype.md)
  The content type of the part, as a Uniform Type Identifier.
- [struct UTType](../uniformtypeidentifiers/uttype-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmspartcontent/mmsdispositiontype)*