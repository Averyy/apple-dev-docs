# propagateAttachments(to:)

**Framework**: Core Media  
**Kind**: method  
**Required**: Yes

Copies all propagable attachments from one attachment bearer object to another.

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
func propagateAttachments<T>(to destination: T) where T : CMAttachmentBearerProtocol
```

## Parameters

- `destination`: The object to copy attachments to.

## See Also

- [var attachments: CMAttachmentBearerAttachments](cmattachmentbearerprotocol/attachments.md)
  All attachments for this object.
- [struct CMAttachmentBearerAttachments](cmattachmentbearerattachments.md)
  A structure that contains attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmattachmentbearerprotocol/propagateattachments(to:))*