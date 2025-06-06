# CMAttachmentBearerProtocol

**Framework**: Core Media  
**Kind**: protocol

A protocol for objects that can carry attachments.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol CMAttachmentBearerProtocol
```

## Topics

### Processing Attachments
- [var attachments: CMAttachmentBearerAttachments](cmattachmentbearerprotocol/attachments.md)
  All attachments for this object.
- [func propagateAttachments<T>(to: T)](cmattachmentbearerprotocol/propagateattachments(to:).md)
  Copies all propagable attachments from one attachment bearer object to another.
- [struct CMAttachmentBearerAttachments](cmattachmentbearerattachments.md)
  A structure that contains attachments.

## Relationships

### Conforming Types
- [CMBlockBuffer](cmblockbuffer.md)
- [CMSampleBuffer](cmsamplebuffer.md)

## See Also

- [typealias CMAttachmentBearer](cmattachmentbearer.md)
  An object that can carry attachments.
- [typealias CMAttachmentMode](cmattachmentmode.md)
  The mode to use when propagating attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmattachmentbearerprotocol)*