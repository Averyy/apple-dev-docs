# UIImagePickerController.SourceType.savedPhotosAlbum

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

Specifies the device’s Camera Roll album as the source for the image picker controller.

**Availability**:
- iOS 2.0+ - Deprecated in 27.0
- iPadOS 2.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`PHPickerViewController`](../../../PhotosUI/phpickerviewcontroller.md) instead.

## Declaration

```swift
case savedPhotosAlbum
```

```c
UIImagePickerControllerSourceTypeSavedPhotosAlbum
```

## Discussion

If the device does not have a camera, specifies the Saved Photos album as the source.

## See Also

### Constants
- [UIImagePickerController.SourceType.camera](./camera.md)
  Specifies the device’s built-in camera as the source for the image picker controller.
- [UIImagePickerController.SourceType.photoLibrary](./photolibrary.md)
  Specifies the device’s photo library as the source for the image picker controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/sourcetype-swift.enum/savedphotosalbum)*