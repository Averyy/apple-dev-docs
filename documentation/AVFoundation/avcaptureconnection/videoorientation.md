# videoOrientation

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An orientation that tells the connection how to rotate a video flowing through it.

**Availability**:
- iOS 4.0+ - Deprecated in 17.0
- iPadOS 4.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 10.7+ - Deprecated in 14.0

> **Deprecated**: See [`videoRotationAngle`](./videorotationangle.md) instead.

## Declaration

```swift
var videoOrientation: AVCaptureVideoOrientation { get set }
```

```objc
@property (nonatomic) AVCaptureVideoOrientation videoOrientation;
```

## Mentions

- [Setting up a capture session](../setting-up-a-capture-session.md)

## Discussion

The property only applies to a video connection.

If the value of [`isVideoOrientationSupported`](./isvideoorientationsupported.md) is [`true`](../../Swift/true.md), you can set `videoOrientation` to rotate the video buffers consumed by the connection’s output. Setting `videoOrientation` doesn’t necessarily result in a physical rotation of video buffers. For example, a video connection to an [`AVCaptureMovieFileOutput`](../avcapturemoviefileoutput.md) object handles orientation using a QuickTime track matrix. A video connection to an [`AVCaptureStillImageOutput`](../avcapturestillimageoutput.md) object handles orientation using Exif tags.

[`AVCaptureVideoDataOutput`](../avcapturevideodataoutput.md) clients may receive physically rotated pixel buffers in their [`captureOutput(_:didOutput:from:)`](../avcapturevideodataoutputsamplebufferdelegate/captureoutput%28_,didoutput,from%29.md) delegate callback. The `AVCaptureVideoDataOutput` hardware accelerates the rotation operation and supports all four [`AVCaptureVideoOrientation`](../avcapturevideoorientation.md) modes. A client sets `videoOrientation` or [`isVideoMirrored`](./isvideomirrored.md) on the video data output’s video [`AVCaptureConnection`](../avcaptureconnection.md) to request physical buffer rotation.

> ❗ **Important**:  Physically rotating buffers comes with a performance cost, so only request rotation when necessary. If you want to write rotated video to a movie file using [`AVAssetWriter`](../avassetwriter.md), set the [`transform`](../avassetwriterinput/transform.md) property on the [`AVAssetWriterInput`](../avassetwriterinput.md) instead.

## See Also

### Deprecated
- [var isVideoStabilizationEnabled: Bool](./isvideostabilizationenabled.md)
  A Boolean value that indicates whether video stabilization is active for the connection.
- [var enablesVideoStabilizationWhenAvailable: Bool](./enablesvideostabilizationwhenavailable.md)
  A Boolean value that indicates whether the system enables video stabilization when it’s available.
- [var isVideoOrientationSupported: Bool](./isvideoorientationsupported.md)
  A Boolean value that indicates whether the connection supports changing the orientation of the video.
- [enum AVCaptureVideoOrientation](../avcapturevideoorientation.md)
  Constants indicating video orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/videoorientation)*