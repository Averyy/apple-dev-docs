# imagePickerController(_:didFinishPickingMediaWithInfo:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the user picked a still image or movie.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any])
```

#### Discussion

Your delegate object’s implementation of this method should pass the specified media on to any custom code that needs it, and should then dismiss the picker view.

When editing is enabled, the image picker view presents the user with a preview of the currently selected image or movie along with controls for modifying it. (This behavior is managed by the picker view prior to calling this method.) If the user modifies the image or movie, the editing information is available in the `info` parameter. The original image is also returned in the `info` parameter.

If you set the image picker’s [`showsCameraControls`](uiimagepickercontroller/showscameracontrols.md) property to [`false`](https://developer.apple.com/documentation/swift/false) and provide your own custom controls, you can take multiple pictures before dismissing the image picker interface. However, if you set that property to [`true`](https://developer.apple.com/documentation/swift/true), your delegate must dismiss the image picker interface after the user takes one picture or cancels the operation.

Implementation of this method is optional, but expected.

## Parameters

- `picker`: The controller object managing the image picker interface.
- `info`: A dictionary containing the original image and the edited image, if an image was picked; or a filesystem URL for the movie, if a movie was picked. The dictionary also contains any relevant editing information. The keys for this dictionary are listed in  .

## See Also

- [func imagePickerControllerDidCancel(UIImagePickerController)](uiimagepickercontrollerdelegate/imagepickercontrollerdidcancel(_:).md)
  Tells the delegate that the user canceled the pick operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate/imagepickercontroller(_:didfinishpickingmediawithinfo:))*