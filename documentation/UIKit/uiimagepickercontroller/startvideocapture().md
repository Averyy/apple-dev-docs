# startVideoCapture()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Starts video capture using the camera specified by the camera device property.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func startVideoCapture() -> Bool
```

```objc
- (BOOL) startVideoCapture;
```

#### Return Value

[`true`](../../Swift/true.md) on success or [`false`](../../Swift/false.md) on failure. This method may return a value of [`false`](../../Swift/false.md) for various reasons, among them the following:

- Movie capture is already in progress
- The device does not support movie capture
- The device is out of disk space

#### Discussion

Use this method in conjunction with a custom overlay view to initiate the programmatic capture of a movie. You can take more than one movie without leaving the interface, but to do so requires you to hide the default image picker controls.

Calling this method while a movie is being captured has no effect. You must call the [`stopVideoCapture()`](./stopvideocapture%28%29.md) method, and then wait until the associated delegate object receives an [`imagePickerController(_:didFinishPickingMediaWithInfo:)`](../uiimagepickercontrollerdelegate/imagepickercontroller%28_,didfinishpickingmediawithinfo%29.md) message, before you can capture another movie.

Calling this method when the source type of the image picker is set to a value other than [`UIImagePickerController.SourceType.camera`](./sourcetype-swift.enum/camera.md) results in the throwing of an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md) exception.

If you require additional options or more control over movie capture, use the movie capture methods in the AVFoundation framework. Refer to [AVFoundation](../../AVFoundation/AVFoundation.md).

## See Also

### Capturing still images or movies
- [func takePicture()](./takepicture%28%29.md)
  Captures a still image using the camera.
- [func stopVideoCapture()](./stopvideocapture%28%29.md)
  Stops video capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/startvideocapture())*