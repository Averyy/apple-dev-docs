# RCSFileTransferMetadata.Disposition

**Framework**: TelephonyMessagingKit  
**Kind**: enum

An enumeration that represents the disposition of the file, indicating how a receiving app should handle it.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
enum Disposition
```

## Topics

### Working with dispositions
- [RCSFileTransferMetadata.Disposition.attachment](rcsfiletransfermetadata/disposition-swift.enum/attachment.md)
  The attachment disposition, directing the receiving app to not automatically render the file.
- [RCSFileTransferMetadata.Disposition.render](rcsfiletransfermetadata/disposition-swift.enum/render.md)
  The render disposition, directing the receiving app to render the file automatically.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsfiletransfermetadata/disposition-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (RCSFileTransferMetadata.Disposition, RCSFileTransferMetadata.Disposition) -> Bool](rcsfiletransfermetadata/disposition-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](rcsfiletransfermetadata/disposition-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](rcsfiletransfermetadata/disposition-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](rcsfiletransfermetadata/disposition-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](rcsfiletransfermetadata/disposition-swift.enum/equatable-implementations.md)

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

- [var disposition: RCSFileTransferMetadata.Disposition?](rcsfiletransfermetadata/disposition-swift.property.md)
  The disposition of the file, indicating how a recipient needs to handle the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsfiletransfermetadata/disposition-swift.enum)*