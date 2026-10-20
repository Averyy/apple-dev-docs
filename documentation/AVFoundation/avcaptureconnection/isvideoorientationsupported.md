# isVideoOrientationSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the connection supports changing the orientation of the video.

**Availability**:
- iOS 4.0+ - Deprecated in 17.0
- iPadOS 4.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 10.7+ - Deprecated in 14.0

> **Deprecated**: Use [`isVideoRotationAngleSupported(_:)`](./isvideorotationanglesupported%28_%29.md) instead.

## Declaration

```swift
var isVideoOrientationSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isVideoOrientationSupported) BOOL supportsVideoOrientation;
```

## See Also

### Deprecated
- [var isVideoStabilizationEnabled: Bool](./isvideostabilizationenabled.md)
  A Boolean value that indicates whether video stabilization is active for the connection.
- [var enablesVideoStabilizationWhenAvailable: Bool](./enablesvideostabilizationwhenavailable.md)
  A Boolean value that indicates whether the system enables video stabilization when it’s available.
- [var videoOrientation: AVCaptureVideoOrientation](./videoorientation.md)
  An orientation that tells the connection how to rotate a video flowing through it.
- [enum AVCaptureVideoOrientation](../avcapturevideoorientation.md)
  Constants indicating video orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/isvideoorientationsupported)*