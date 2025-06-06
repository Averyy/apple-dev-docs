# CMAttachmentMode

**Framework**: Core Media  
**Kind**: typealias

The mode to use when propagating attachments.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias CMAttachmentMode = UInt32
```

#### Discussion

Set these attributes when adding attachments to a [`CMAttachmentBearer`](cmattachmentbearer.md) object.

## Topics

### Modes
- [var kCMAttachmentMode_ShouldNotPropagate: CMAttachmentMode](kcmattachmentmode_shouldnotpropagate.md)
  A mode that doesn’t propagate attachments to another object.
- [var kCMAttachmentMode_ShouldPropagate: CMAttachmentMode](kcmattachmentmode_shouldpropagate.md)
  A mode that propagates attachments to another object.

## See Also

- [protocol CMAttachmentBearerProtocol](cmattachmentbearerprotocol.md)
  A protocol for objects that can carry attachments.
- [typealias CMAttachmentBearer](cmattachmentbearer.md)
  An object that can carry attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmattachmentmode)*