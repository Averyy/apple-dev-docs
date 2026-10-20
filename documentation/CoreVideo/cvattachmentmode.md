# CVAttachmentMode

**Framework**: Core Video  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum CVAttachmentMode : uint32_t;
```

#### Overview

You set these attributes when adding attachments to a [`CVBuffer`](./cvbuffer.md) object.

## Topics

### Constants
- [CVAttachmentMode.shouldNotPropagate](./cvattachmentmode/shouldnotpropagate.md)
  Indicates to not propagate the attachment.
- [CVAttachmentMode.shouldPropagate](./cvattachmentmode/shouldpropagate.md)
  Indicates to copy the attachment.
### Initializers
- [init?(rawValue: UInt32)](./cvattachmentmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Data types
- [class CVBuffer](./cvbuffer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentmode)*