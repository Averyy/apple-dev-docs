# enablesVideoStabilizationWhenAvailable

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the system enables video stabilization when it’s available.

**Availability**:
- iOS 6.0+ - Deprecated in 8.0
- iPadOS 6.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`preferredVideoStabilizationMode`](./preferredvideostabilizationmode.md) property instead.

## Declaration

```swift
var enablesVideoStabilizationWhenAvailable: Bool { get set }
```

```objc
@property (nonatomic) BOOL enablesVideoStabilizationWhenAvailable;
```

## See Also

### Deprecated
- [var isVideoStabilizationEnabled: Bool](./isvideostabilizationenabled.md)
  A Boolean value that indicates whether video stabilization is active for the connection.
- [var isVideoOrientationSupported: Bool](./isvideoorientationsupported.md)
  A Boolean value that indicates whether the connection supports changing the orientation of the video.
- [var videoOrientation: AVCaptureVideoOrientation](./videoorientation.md)
  An orientation that tells the connection how to rotate a video flowing through it.
- [enum AVCaptureVideoOrientation](../avcapturevideoorientation.md)
  Constants indicating video orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/enablesvideostabilizationwhenavailable)*