# AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the replacement policy when a video frame is dropped.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
enum DroppedFrameReplacementPolicy
```

```c
enum AVCaptureBroadcastVideoOutputDroppedFrameReplacementPolicy : NSInteger;
```

#### Overview

These constants specify how the broadcast video output should handle dropped frames by providing replacement content.

## Topics

### Enumeration Cases
- [AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy.blackFrame](./droppedframereplacementpolicy-swift.enum/blackframe.md)
  Insert a black frame as replacement. When a frame is dropped, a black frame is inserted at the expected presentation time. This maintains output timing continuity while providing a clear visual indication of the dropped frame.
- [AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy.repeatPreviousFrame](./droppedframereplacementpolicy-swift.enum/repeatpreviousframe.md)
  Repeat the previous frame as replacement. When a frame is dropped, the most recent successfully output frame is repeated at the expected presentation time. This is the default behavior and provides smoother visual continuity.
### Initializers
- [init?(rawValue: Int)](./droppedframereplacementpolicy-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum)*