# RCSFileTransferMetadata.Disposition

**Framework**: TelephonyMessagingKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration that represents the disposition of the file, indicating how a receiving app should handle it.

**Availability**:
- iOS 26.0+

## Declaration

```swift
enum Disposition
```

## Topics

### Working with dispositions
- [RCSFileTransferMetadata.Disposition.attachment](./disposition-swift.enum/attachment.md)
  The attachment disposition, directing the receiving app to not automatically render the file.
- [RCSFileTransferMetadata.Disposition.render](./disposition-swift.enum/render.md)
  The render disposition, directing the receiving app to render the file automatically.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Working with file disposition
- [var disposition: RCSFileTransferMetadata.Disposition?](./disposition-swift.property.md)
  The disposition of the file, indicating how a recipient needs to handle the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsfiletransfermetadata/disposition-swift.enum)*