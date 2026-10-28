# takePicture()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Captures a still image using the camera.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+

## Declaration

```swift
func takePicture()
```

```objc
- (void) takePicture;
```

## Discussion

Use this method in conjunction with a custom overlay view to initiate the programmatic capture of a still image. This supports taking more than one picture without leaving the interface, but requires that you hide the default image picker controls.

Calling this method while an image is being captured has no effect. You must wait until the associated delegate object receives an [`imagePickerController(_:didFinishPickingMediaWithInfo:)`](../uiimagepickercontrollerdelegate/imagepickercontroller%28_,didfinishpickingmediawithinfo%29.md) message before you can capture another picture.

Calling this method when the source type of the image picker is set to a value other than [`UIImagePickerController.SourceType.camera`](./sourcetype-swift.enum/camera.md) results in the throwing of an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md) exception.

## See Also

### Related Documentation
- [var cameraOverlayView: UIView?](./cameraoverlayview.md)
  The view to display on top of the default image picker interface.
### Capturing still images or movies
- [func startVideoCapture() -> Bool](./startvideocapture%28%29.md)
  Starts video capture using the camera specified by the camera device property.
- [func stopVideoCapture()](./stopvideocapture%28%29.md)
  Stops video capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/takepicture())*