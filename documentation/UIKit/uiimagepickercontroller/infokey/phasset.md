# phAsset

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A Photos asset for the image.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`PHPickerViewController`](../../../PhotosUI/phpickerviewcontroller.md) instead.

## Declaration

```swift
static let phAsset: UIImagePickerController.InfoKey
```

```c
extern UIImagePickerControllerInfoKey const UIImagePickerControllerPHAsset;
```

#### Discussion

The value of this key is a [`PHAsset`](../../../Photos/phasset.md) object.

## See Also

### Constants
- [static let cropRect: UIImagePickerController.InfoKey](./croprect.md)
  The cropping rectangle that was applied to the original image.
- [static let editedImage: UIImagePickerController.InfoKey](./editedimage.md)
  An image edited by the user.
- [static let imageURL: UIImagePickerController.InfoKey](./imageurl.md)
  The URL of the image file.
- [static let livePhoto: UIImagePickerController.InfoKey](./livephoto.md)
  The Live Photo representation of the selected or captured photo.
- [static let mediaMetadata: UIImagePickerController.InfoKey](./mediametadata.md)
  Metadata for a newly-captured photograph.
- [static let mediaType: UIImagePickerController.InfoKey](./mediatype.md)
  The media type selected by the user.
- [static let mediaURL: UIImagePickerController.InfoKey](./mediaurl.md)
  The filesystem URL for the movie.
- [static let originalImage: UIImagePickerController.InfoKey](./originalimage.md)
  The original, uncropped image selected by the user.
- [static let referenceURL: UIImagePickerController.InfoKey](./referenceurl.md)
  The Assets Library URL for the original version of the picked item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey/phasset)*