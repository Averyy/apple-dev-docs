# CMDroppedFrameReason

**Framework**: Core Media  
**Kind**: enum

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum CMDroppedFrameReason
```

## Topics

### Enumeration Cases
- [CMDroppedFrameReason.discontinuity](cmdroppedframereason/discontinuity.md)
  An unknown number of frames were dropped.
- [CMDroppedFrameReason.frameWasLate](cmdroppedframereason/framewaslate.md)
  The frame was dropped because it was late.
- [CMDroppedFrameReason.outOfBuffers](cmdroppedframereason/outofbuffers.md)
  The frame was dropped because the module providing frames is out of buffers.
### Enumerations
- [CMDroppedFrameReason.Info](cmdroppedframereason/info.md)
  Provides additional information regarding the dropped video frame.

## Relationships

### Conforms To
- [CVAttachmentValueRepresentable](../CoreVideo/CVAttachmentValueRepresentable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmdroppedframereason)*