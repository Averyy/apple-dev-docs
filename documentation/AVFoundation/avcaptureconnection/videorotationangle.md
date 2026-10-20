# videoRotationAngle

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A rotation angle the connection applies to the video flowing through it.

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

```objc
@property (nonatomic) CGFloat videoRotationAngle;
```

#### Discussion

Set this property to an angle that an [`AVCaptureDevice.RotationCoordinator`](../avcapturedevice/rotationcoordinator.md) instance provides to keep video level relative to gravity. Only `0`, `90`, `180`, and `270` are valid angles. Setting any other value raises an `NSInvalidArgumentException`, so confirm that a connection supports an angle with [`isVideoRotationAngleSupported(_:)`](./isvideorotationanglesupported%28_%29.md). The property applies only to video and depth connections.

Setting an angle doesn’t always rotate pixels. A connection to an [`AVCaptureMovieFileOutput`](../avcapturemoviefileoutput.md) instance records the rotation in a QuickTime track matrix, and a connection to an [`AVCapturePhotoOutput`](../avcapturephotooutput.md) instance records it in Exif tags. Connections to [`AVCaptureVideoDataOutput`](../avcapturevideodataoutput.md) and [`AVCaptureDepthDataOutput`](../avcapturedepthdataoutput.md) instances deliver physically rotated buffers instead, which costs work on every frame. Setting an angle on those connections also reconfigures the capture render pipeline, so set it before calling [`startRunning()`](../avcapturesession/startrunning%28%29.md).

If your app rotates buffers itself, set `videoRotationAngle` to `0` to keep the connection from rotating them again. If your app applies a coordinator’s angles with its own math, account for the property’s current value. Account for it on every device rather than only the devices where the default differs, which keeps the same code correct as hardware changes.

A connection doesn’t rotate ProRes RAW buffers. When your app captures ProRes RAW, set this property to `0` and apply a coordinator’s angles to those buffers yourself.

To rotate a movie that your app writes with an [`AVAssetWriter`](../avassetwriter.md) instance, set [`transform`](../avassetwriterinput/transform.md) rather than rotating through the connection, which avoids paying for a rotation on every frame.

> **Note**:  Transform properties take radians, so convert a coordinator’s angle before you apply it.

## See Also

### Rotating a video
- [func isVideoRotationAngleSupported(CGFloat) -> Bool](./isvideorotationanglesupported%28_%29.md)
  Returns a Boolean value that indicates whether the connection supports a rotation angle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/videorotationangle)*