# imagePickerControllerDidCancel(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user canceled the pick operation.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func imagePickerControllerDidCancel(_ picker: UIImagePickerController)
```

```objc
- (void) imagePickerControllerDidCancel:(UIImagePickerController *) picker;
```

#### Discussion

Your delegate’s implementation of this method should dismiss the picker view by calling the [`dismiss(animated:completion:)`](../uiviewcontroller/dismiss%28animated,completion%29.md) method of the parent view controller.

Implementation of this method is optional, but expected.

## Parameters

- `picker`: The controller object managing the image picker interface.

## See Also

### Closing the picker
- [func imagePickerController(UIImagePickerController, didFinishPickingMediaWithInfo: [UIImagePickerController.InfoKey : Any])](./imagepickercontroller%28_,didfinishpickingmediawithinfo%29.md)
  Tells the delegate that the user picked a still image or movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate/imagepickercontrollerdidcancel(_:))*