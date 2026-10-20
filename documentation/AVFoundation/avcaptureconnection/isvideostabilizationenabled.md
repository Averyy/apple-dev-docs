# isVideoStabilizationEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether video stabilization is active for the connection.

**Availability**:
- iOS 6.0+ - Deprecated in 8.0
- iPadOS 6.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`activeVideoStabilizationMode`](./activevideostabilizationmode.md) property instead.

## Declaration

```swift
var isVideoStabilizationEnabled: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isVideoStabilizationEnabled) BOOL videoStabilizationEnabled;
```

## See Also

### Deprecated
- [var enablesVideoStabilizationWhenAvailable: Bool](./enablesvideostabilizationwhenavailable.md)
  A Boolean value that indicates whether the system enables video stabilization when it’s available.
- [var isVideoOrientationSupported: Bool](./isvideoorientationsupported.md)
  A Boolean value that indicates whether the connection supports changing the orientation of the video.
- [var videoOrientation: AVCaptureVideoOrientation](./videoorientation.md)
  An orientation that tells the connection how to rotate a video flowing through it.
- [enum AVCaptureVideoOrientation](../avcapturevideoorientation.md)
  Constants indicating video orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/isvideostabilizationenabled)*