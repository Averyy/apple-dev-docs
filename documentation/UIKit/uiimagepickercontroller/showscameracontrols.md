# showsCameraControls

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the image picker displays the default camera controls.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var showsCameraControls: Bool { get set }
```

#### Discussion

The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true), which specifies that the default camera controls are visible in the picker. Set it to [`false`](https://developer.apple.com/documentation/swift/false) to hide the default controls if you want to instead provide a custom overlay view using the [`cameraOverlayView`](uiimagepickercontroller/cameraoverlayview.md) property.

> **Note**:  In iOS 3.1.3 and earlier, hiding the default camera controls limits you to taking still pictures only, regardless of whether movie capture is available on the device.

 In iOS 3.1.3 and earlier, hiding the default camera controls limits you to taking still pictures only, regardless of whether movie capture is available on the device.

If you set this property to [`false`](https://developer.apple.com/documentation/swift/false) and provide your own custom controls, you can take multiple pictures before dismissing the image picker interface. However, if you set this property to [`true`](https://developer.apple.com/documentation/swift/true), your delegate must dismiss the image picker interface after the user takes one picture or cancels the operation.

You can access this property only when the source type of the image picker is set to [`UIImagePickerController.SourceType.camera`](uiimagepickercontroller/sourcetype-swift.enum/camera.md). Attempting to access this property for other source types results in the throwing of an [`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1415426-invalidargumentexception) exception. Depending on the value you assign to the [`mediaTypes`](uiimagepickercontroller/mediatypes.md) property, the default controls display the still camera or movie camera interface, or a selection control that lets the user choose the picker interface.

## See Also

- [func takePicture()](uiimagepickercontroller/takepicture.md)
  Captures a still image using the camera.
- [Customizing an image picker controller](customizing-an-image-picker-controller.md)
  Manage user interactions and present custom information when taking pictures by adding an overlay view to your image picker.
- [var cameraOverlayView: UIView?](uiimagepickercontroller/cameraoverlayview.md)
  The view to display on top of the default image picker interface.
- [var cameraViewTransform: CGAffineTransform](uiimagepickercontroller/cameraviewtransform.md)
  The transform to apply to the camera’s preview image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/showscameracontrols)*