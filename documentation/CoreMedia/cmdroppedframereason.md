# CMDroppedFrameReason

**Framework**: Core Media  
**Kind**: enum

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
- [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md)
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmdroppedframereason)*