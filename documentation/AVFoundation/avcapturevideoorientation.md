# AVCaptureVideoOrientation

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants indicating video orientation.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 10.7+ - Deprecated in 14.0

> **Deprecated**: See [`videoRotationAngle`](./avcaptureconnection/videorotationangle.md) instead.

## Declaration

```swift
enum AVCaptureVideoOrientation
```

```c
enum AVCaptureVideoOrientation : NSInteger;
```

#### Overview

You can set these constants to [`videoOrientation`](./avcaptureconnection/videoorientation.md) for a connection that has an [`AVCaptureVideoPreviewLayer`](./avcapturevideopreviewlayer.md) output.

## Topics

### Constants
- [AVCaptureVideoOrientation.portrait](./avcapturevideoorientation/portrait.md)
  Indicates that video should be oriented vertically, top at the top.
- [AVCaptureVideoOrientation.portraitUpsideDown](./avcapturevideoorientation/portraitupsidedown.md)
  Indicates that video should be oriented vertically, top at the bottom.
- [AVCaptureVideoOrientation.landscapeRight](./avcapturevideoorientation/landscaperight.md)
  Indicates that video should be oriented horizontally, top on the left.
- [AVCaptureVideoOrientation.landscapeLeft](./avcapturevideoorientation/landscapeleft.md)
  Indicates that video should be oriented horizontally, top on the right.
### Initializers
- [init?(rawValue: Int)](./avcapturevideoorientation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deprecated
- [var isVideoStabilizationEnabled: Bool](./avcaptureconnection/isvideostabilizationenabled.md)
  A Boolean value that indicates whether video stabilization is active for the connection.
- [var enablesVideoStabilizationWhenAvailable: Bool](./avcaptureconnection/enablesvideostabilizationwhenavailable.md)
  A Boolean value that indicates whether the system enables video stabilization when it’s available.
- [var isVideoOrientationSupported: Bool](./avcaptureconnection/isvideoorientationsupported.md)
  A Boolean value that indicates whether the connection supports changing the orientation of the video.
- [var videoOrientation: AVCaptureVideoOrientation](./avcaptureconnection/videoorientation.md)
  An orientation that tells the connection how to rotate a video flowing through it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideoorientation)*