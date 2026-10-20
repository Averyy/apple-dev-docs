# stopVideoCapture()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Stops video capture.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func stopVideoCapture()
```

```objc
- (void) stopVideoCapture;
```

#### Discussion

After you call this method to stop video capture, the system calls the image picker delegate’s [`imagePickerController(_:didFinishPickingMediaWithInfo:)`](../uiimagepickercontrollerdelegate/imagepickercontroller%28_,didfinishpickingmediawithinfo%29.md) method.

## See Also

### Capturing still images or movies
- [func takePicture()](./takepicture%28%29.md)
  Captures a still image using the camera.
- [func startVideoCapture() -> Bool](./startvideocapture%28%29.md)
  Starts video capture using the camera specified by the camera device property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/stopvideocapture())*