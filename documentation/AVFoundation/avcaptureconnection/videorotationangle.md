# videoRotationAngle

**Framework**: AVFoundation  
**Kind**: property

A rotation angle the connection applies to a video flowing through it.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
var videoRotationAngle: CGFloat { get set }
```

#### Discussion

Your app can set a video rotation angle that it gets from an [`AVCaptureDevice.RotationCoordinator`](avcapturedevice/rotationcoordinator.md) instance’s [`videoRotationAngleForHorizonLevelCapture`](avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelcapture.md) or [`videoRotationAngleForHorizonLevelPreview`](avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelpreview.md) property. The rotation angle only applies to video or depth connections, similar to [`isVideoMirrored`](avcaptureconnection/isvideomirrored.md), and can be any angle that [`isVideoRotationAngleSupported(_:)`](avcaptureconnection/isvideorotationanglesupported(_:).md) returns [`true`](https://developer.apple.com/documentation/swift/true) for.

Not all capture connections rotate each frame. For example, a video connection to an [`AVCaptureMovieFileOutput`](avcapturemoviefileoutput.md) or [`AVCapturePhotoOutput`](avcapturephotooutput.md) instance applies a rotation with a QuickTime track matrix or with EXIF tags, respectively.

Capture connections to [`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md) and [`AVCaptureDepthDataOutput`](avcapturedepthdataoutput.md) instances rotate video frames they provide to their [`captureOutput(_:didOutput:from:)`](avcapturevideodataoutputsamplebufferdelegate/captureoutput(_:didoutput:from:).md) and [`depthDataOutput(_:didOutput:timestamp:connection:)`](avcapturedepthdataoutputdelegate/depthdataoutput(_:didoutput:timestamp:connection:).md) delegate methods, respectively. Each [`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md) instance uses hardware acceleration to rotate every frame.

> 💡 **Tip**:  Avoid potential performance issues by only rotating video with a capture connection when necessary.

 Avoid potential performance issues by only rotating video with a capture connection when necessary.

You can rotate the video of a movie file you record with an [`AVAssetWriter`](avassetwriter.md) instance by applying the rotation to an [`AVAssetWriterInput`](avassetwriterinput.md) instance’s [`transform`](avassetwriterinput/transform.md) property. This approach avoids the performance costs that come with rotating each video frame.

> **Note**:  Your app needs to convert the [`videoRotationAngleForHorizonLevelCapture`](avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelcapture.md) or [`videoRotationAngleForHorizonLevelPreview`](avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelpreview.md) value from degrees to radians for transform properties.

 Your app needs to convert the [`videoRotationAngleForHorizonLevelCapture`](avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelcapture.md) or [`videoRotationAngleForHorizonLevelPreview`](avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelpreview.md) value from degrees to radians for transform properties.

## See Also

- [func isVideoRotationAngleSupported(CGFloat) -> Bool](avcaptureconnection/isvideorotationanglesupported(_:).md)
  Returns a Boolean value that indicates whether the connection supports a rotation angle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/videorotationangle)*