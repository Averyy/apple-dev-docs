# cameraViewTransform

**Framework**: UIKit  
**Kind**: property

The transform to apply to the camera’s preview image.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var cameraViewTransform: CGAffineTransform { get set }
```

#### Discussion

This transform affects the live preview image only and does not affect your custom overlay view or the default image picker controls. You can use this property in conjunction with custom controls to implement your own electronic zoom behaviors.

You can access this property only when the source type of the image picker is set to [`UIImagePickerController.SourceType.camera`](uiimagepickercontroller/sourcetype-swift.enum/camera.md). Attempting to access this property for other source types results in the throwing of an [`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1415426-invalidargumentexception) exception.

## See Also

- [Customizing an image picker controller](customizing-an-image-picker-controller.md)
  Manage user interactions and present custom information when taking pictures by adding an overlay view to your image picker.
- [var showsCameraControls: Bool](uiimagepickercontroller/showscameracontrols.md)
  A Boolean value that indicates whether the image picker displays the default camera controls.
- [var cameraOverlayView: UIView?](uiimagepickercontroller/cameraoverlayview.md)
  The view to display on top of the default image picker interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameraviewtransform)*