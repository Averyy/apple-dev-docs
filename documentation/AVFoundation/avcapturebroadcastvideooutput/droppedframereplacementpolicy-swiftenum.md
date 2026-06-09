# AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy

**Framework**: AVFoundation  
**Kind**: enum

Constants indicating the replacement policy when a video frame is dropped.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
enum DroppedFrameReplacementPolicy
```

#### Overview

These constants specify how the broadcast video output should handle dropped frames by providing replacement content.

## Topics

### Enumeration Cases
- [AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy.blackFrame](avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum/blackframe.md)
  Insert a black frame as replacement. When a frame is dropped, a black frame is inserted at the expected presentation time. This maintains output timing continuity while providing a clear visual indication of the dropped frame.
- [AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy.repeatPreviousFrame](avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum/repeatpreviousframe.md)
  Repeat the previous frame as replacement. When a frame is dropped, the most recent successfully output frame is repeated at the expected presentation time. This is the default behavior and provides smoother visual continuity.
### Initializers
- [init?(rawValue: Int)](avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum)*