# MMSPartContent.MMSDispositionType

**Framework**: TelephonyMessagingKit  
**Kind**: enum

A structure that defines the disposition of the content part when rendered.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
enum MMSDispositionType
```

## Topics

### Operators
- [static func == (MMSPartContent.MMSDispositionType, MMSPartContent.MMSDispositionType) -> Bool](mmspartcontent/mmsdispositiontype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [MMSPartContent.MMSDispositionType.attachment](mmspartcontent/mmsdispositiontype/attachment.md)
  A disposition to render the content part as an attachment to the message.
- [MMSPartContent.MMSDispositionType.inline](mmspartcontent/mmsdispositiontype/inline.md)
  A disposition to render the content part in line with the rest of the message.
### Initializers
- [init(from: any Decoder) throws](mmspartcontent/mmsdispositiontype/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](mmspartcontent/mmsdispositiontype/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](mmspartcontent/mmsdispositiontype/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](mmspartcontent/mmsdispositiontype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mmspartcontent/mmsdispositiontype/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [struct UTType](../UniformTypeIdentifiers/UTType-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmspartcontent/mmsdispositiontype)*