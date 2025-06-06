# videoOrientation

**Framework**: AVFoundation  
**Kind**: property

An orientation that tells the connection how to rotate a video flowing through it.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+

## Declaration

```swift
var videoOrientation: AVCaptureVideoOrientation { get set }
```

## Mentions

- [Setting Up a Capture Session](setting-up-a-capture-session.md)

#### Discussion

The property only applies to a video connection.

If the value of [`isVideoOrientationSupported`](avcaptureconnection/isvideoorientationsupported.md) is [`true`](https://developer.apple.com/documentation/swift/true), you can set `videoOrientation` to rotate the video buffers consumed by the connection’s output. Setting `videoOrientation` doesn’t necessarily result in a physical rotation of video buffers. For example, a video connection to an [`AVCaptureMovieFileOutput`](avcapturemoviefileoutput.md) object handles orientation using a QuickTime track matrix. A video connection to an [`AVCaptureStillImageOutput`](avcapturestillimageoutput.md) object handles orientation using EXIF tags.

[`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md) clients may receive physically rotated pixel buffers in their [`captureOutput(_:didOutput:from:)`](avcapturevideodataoutputsamplebufferdelegate/captureoutput(_:didoutput:from:).md) delegate callback. The `AVCaptureVideoDataOutput` hardware accelerates the rotation operation and supports all four [`AVCaptureVideoOrientation`](avcapturevideoorientation.md) modes. A client sets `videoOrientation` or [`isVideoMirrored`](avcaptureconnection/isvideomirrored.md) on the video data output’s video [`AVCaptureConnection`](avcaptureconnection.md) to request physical buffer rotation.

> ❗ **Important**:  Physically rotating buffers comes with a performance cost, so only request rotation when necessary. If you want to write rotated video to a movie file using [`AVAssetWriter`](avassetwriter.md), set the [`transform`](avassetwriterinput/transform.md) property on the [`AVAssetWriterInput`](avassetwriterinput.md) instead.

 Physically rotating buffers comes with a performance cost, so only request rotation when necessary. If you want to write rotated video to a movie file using [`AVAssetWriter`](avassetwriter.md), set the [`transform`](avassetwriterinput/transform.md) property on the [`AVAssetWriterInput`](avassetwriterinput.md) instead.

## See Also

- [var isVideoStabilizationEnabled: Bool](avcaptureconnection/isvideostabilizationenabled.md)
  A Boolean value that indicates whether video stabilization is active for the connection.
- [var enablesVideoStabilizationWhenAvailable: Bool](avcaptureconnection/enablesvideostabilizationwhenavailable.md)
  A Boolean value that indicates whether the system enables video stabilization when it’s available.
- [var isVideoOrientationSupported: Bool](avcaptureconnection/isvideoorientationsupported.md)
  A Boolean value that indicates whether the connection supports changing the orientation of the video.
- [enum AVCaptureVideoOrientation](avcapturevideoorientation.md)
  Constants indicating video orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/videoorientation)*