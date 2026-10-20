# referenceURL

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The Assets Library URL for the original version of the picked item.

**Availability**:
- iOS 4.1+ - Deprecated in 11.0
- iPadOS 4.1+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`PHPickerViewController`](https://developer.apple.com/documentation/photosui/phpickerviewcontroller) instead.

## Declaration

```swift
static let referenceURL: UIImagePickerController.InfoKey
```

```c
extern UIImagePickerControllerInfoKey const UIImagePickerControllerReferenceURL;
```

#### Discussion

After the user edits a picked item—such as by cropping an image or trimming a movie—the URL continues to point to the original version of the picked item.

The value for this key is an [`NSURL`](../../../Foundation/nsurl.md) object.

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
- [static let phAsset: UIImagePickerController.InfoKey](./phasset.md)
  A Photos asset for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey/referenceurl)*