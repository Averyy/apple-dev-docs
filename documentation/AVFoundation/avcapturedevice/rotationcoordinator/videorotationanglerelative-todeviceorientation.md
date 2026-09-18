# videoRotationAngleRelative(toDeviceOrientation:)

**Framework**: AVFoundation  
**Kind**: method

An angle the coordinator provides your app to apply to photos or videos it takes with the capture device so that they’re upright relative to an orientation your app provides.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
func videoRotationAngleRelative(toDeviceOrientation deviceOrientation: AVCaptureVideoOrientation) -> CGFloat
```

#### Discussion

The angle this method returns is distinct from the angles that the [`videoRotationAngleForHorizonLevelPreview`](avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelpreview.md) and [`videoRotationAngleForHorizonLevelCapture`](avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelcapture.md) properties provide. Those angles are relative to the horizon and change dynamically as someone physically rotates the device. This method returns a static angle relative to the orientation your app provides, no matter how the device is physically oriented when your app calls it.

An angle of `0` means the output is in the camera’s unrotated, native sensor orientation. Cameras vary in how they’re physically mounted. The angle for an orientation may differ between the capture devices your app uses. An external camera returns `0` for every orientation because the relationship between the device and the camera is unknown.

Apps typically apply the returned angle to an [`AVCaptureConnection`](avcaptureconnection.md) instance’s [`videoRotationAngle`](avcaptureconnection/videorotationangle.md) property, which describes the angles a connection accepts and how it applies them.

## Parameters

- `deviceOrientation`: The device orientation to measure the angle against, represented with the [`AVCaptureVideoOrientation`](avcapturevideoorientation.md) enumeration.

## See Also

- [var videoRotationAngleForHorizonLevelCapture: CGFloat](avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelcapture.md)
  An angle the coordinator provides your app to apply to photos or videos it captures with the device so that they’re level relative to gravity.
- [var videoRotationAngleForHorizonLevelPreview: CGFloat](avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelpreview.md)
  An angle the coordinator provides your app to apply to the preview layer so that it’s level relative to gravity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator/videorotationanglerelative(todeviceorientation:))*