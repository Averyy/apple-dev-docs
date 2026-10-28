# UIImagePickerControllerDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods that your delegate object must implement to interact with the image picker interface.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
@MainActor
protocol UIImagePickerControllerDelegate : NSObjectProtocol
```

```objc
@protocol UIImagePickerControllerDelegate <NSObject>
```

## Overview

The methods of this protocol notify your delegate when the user either picks an image or movie, or cancels the picker operation. The delegate methods are responsible for dismissing the picker when the operation completes. To dismiss the picker, call the [`dismiss(animated:completion:)`](./uiviewcontroller/dismiss%28animated,completion%29.md) method of the parent controller responsible for displaying the [`UIImagePickerController`](./uiimagepickercontroller.md) object.

To save a still image to the user’s Camera Roll album, call the [`UIImageWriteToSavedPhotosAlbum(_:_:_:_:)`](./uiimagewritetosavedphotosalbum%28_,_,_,_%29.md) function from within the body of the [`imagePickerController(_:didFinishPickingMediaWithInfo:)`](./uiimagepickercontrollerdelegate/imagepickercontroller%28_,didfinishpickingmediawithinfo%29.md) method. To save a movie to the user’s Camera Roll album, instead call the [`UISaveVideoAtPathToSavedPhotosAlbum(_:_:_:_:)`](./uisavevideoatpathtosavedphotosalbum%28_,_,_,_%29.md) function. These functions, described in `UIKit Functions`, save the image or movie only; they don’t save metadata.

To write additional metadata when saving an image to the Camera Roll, use the [`PHAssetChangeRequest`](../Photos/phassetchangerequest.md) class from the Photos framework. See the description for the [`mediaMetadata`](./uiimagepickercontroller/infokey/mediametadata.md) key.

## Topics

### Closing the picker
- [func imagePickerController(UIImagePickerController, didFinishPickingMediaWithInfo: [UIImagePickerController.InfoKey : Any])](./uiimagepickercontrollerdelegate/imagepickercontroller%28_,didfinishpickingmediawithinfo%29.md)
  Tells the delegate that the user picked a still image or movie.
- [func imagePickerControllerDidCancel(UIImagePickerController)](./uiimagepickercontrollerdelegate/imagepickercontrollerdidcancel%28_%29.md)
  Tells the delegate that the user canceled the pick operation.
- [- imagePickerController:didFinishPickingImage:editingInfo:](./uiimagepickercontrollerdelegate/imagepickercontroller_didfinishpickingimage_editinginfo_.md)
  Tells the delegate that the user picked an image.
### Getting the editing information
- [UIImagePickerController.InfoKey](./uiimagepickercontroller/infokey.md)
  Keys you use to retrieve information from the editing dictionary about the media that the user selected.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to interactions with the picker
- [var delegate: (any UIImagePickerControllerDelegate & UINavigationControllerDelegate)?](./uiimagepickercontroller/delegate.md)
  The image picker’s delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate)*