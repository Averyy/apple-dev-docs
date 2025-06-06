# CVAttachmentMode

**Framework**: Core Video  
**Kind**: enum

The propagation modes of a Core Video buffer attachment.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum CVAttachmentMode
```

#### Overview

You set these attributes when adding attachments to a [`CVBuffer`](cvbuffer.md) object.

## Topics

### Constants
- [CVAttachmentMode.shouldNotPropagate](cvattachmentmode/shouldnotpropagate.md)
  Indicates to not propagate the attachment.
- [CVAttachmentMode.shouldPropagate](cvattachmentmode/shouldpropagate.md)
  Indicates to copy the attachment.
### Initializers
- [init?(rawValue: UInt32)](cvattachmentmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class CVBuffer](cvbuffer.md)
  A reference to a Core Video buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentmode)*