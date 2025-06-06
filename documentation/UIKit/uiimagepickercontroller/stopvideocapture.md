# stopVideoCapture()

**Framework**: UIKit  
**Kind**: method

Stops video capture.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func stopVideoCapture()
```

#### Discussion

After you call this method to stop video capture, the system calls the image picker delegate’s [`imagePickerController(_:didFinishPickingMediaWithInfo:)`](uiimagepickercontrollerdelegate/imagepickercontroller(_:didfinishpickingmediawithinfo:).md) method.

## See Also

- [func takePicture()](uiimagepickercontroller/takepicture.md)
  Captures a still image using the camera.
- [func startVideoCapture() -> Bool](uiimagepickercontroller/startvideocapture.md)
  Starts video capture using the camera specified by the camera device property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/stopvideocapture())*