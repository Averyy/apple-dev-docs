# AVCaptureVideoOrientation

**Framework**: AVFoundation  
**Kind**: enum

Constants indicating video orientation.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+

## Declaration

```swift
enum AVCaptureVideoOrientation
```

#### Overview

You can set these constants to [`videoOrientation`](avcaptureconnection/videoorientation.md) for a connection that has an [`AVCaptureVideoPreviewLayer`](avcapturevideopreviewlayer.md) output.

## Topics

### Constants
- [AVCaptureVideoOrientation.portrait](avcapturevideoorientation/portrait.md)
  Indicates that video should be oriented vertically, top at the top.
- [AVCaptureVideoOrientation.portraitUpsideDown](avcapturevideoorientation/portraitupsidedown.md)
  Indicates that video should be oriented vertically, top at the bottom.
- [AVCaptureVideoOrientation.landscapeRight](avcapturevideoorientation/landscaperight.md)
  Indicates that video should be oriented horizontally, top on the left.
- [AVCaptureVideoOrientation.landscapeLeft](avcapturevideoorientation/landscapeleft.md)
  Indicates that video should be oriented horizontally, top on the right.
### Initializers
- [init?(rawValue: Int)](avcapturevideoorientation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isVideoStabilizationEnabled: Bool](avcaptureconnection/isvideostabilizationenabled.md)
  A Boolean value that indicates whether video stabilization is active for the connection.
- [var enablesVideoStabilizationWhenAvailable: Bool](avcaptureconnection/enablesvideostabilizationwhenavailable.md)
  A Boolean value that indicates whether the system enables video stabilization when it’s available.
- [var isVideoOrientationSupported: Bool](avcaptureconnection/isvideoorientationsupported.md)
  A Boolean value that indicates whether the connection supports changing the orientation of the video.
- [var videoOrientation: AVCaptureVideoOrientation](avcaptureconnection/videoorientation.md)
  An orientation that tells the connection how to rotate a video flowing through it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideoorientation)*