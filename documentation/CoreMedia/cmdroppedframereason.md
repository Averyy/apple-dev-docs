# CMDroppedFrameReason

**Framework**: Core Media  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum CMDroppedFrameReason
```

## Topics

### Enumeration Cases
- [CMDroppedFrameReason.discontinuity](./cmdroppedframereason/discontinuity.md)
  An unknown number of frames were dropped.
- [CMDroppedFrameReason.frameWasLate](./cmdroppedframereason/framewaslate.md)
  The frame was dropped because it was late.
- [CMDroppedFrameReason.outOfBuffers](./cmdroppedframereason/outofbuffers.md)
  The frame was dropped because the module providing frames is out of buffers.
### Enumerations
- [CMDroppedFrameReason.Info](./cmdroppedframereason/info.md)
  Provides additional information regarding the dropped video frame.

## Relationships

### Conforms To
- [CVAttachmentValueRepresentable](../CoreVideo/cvattachmentvaluerepresentable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmdroppedframereason)*