# RCSFileTransferMetadata.Disposition

**Framework**: TelephonyMessagingKit  
**Kind**: enum

An enumeration that represents the disposition of the file, indicating how a receiving app should handle it.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
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