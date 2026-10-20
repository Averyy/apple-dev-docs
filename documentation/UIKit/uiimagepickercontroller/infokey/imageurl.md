# imageURL

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The URL of the image file.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
static let imageURL: UIImagePickerController.InfoKey
```

```c
extern UIImagePickerControllerInfoKey const UIImagePickerControllerImageURL;
```

#### Discussion

The value of this key is a [`NSURL`](../../../Foundation/nsurl.md) that you can use to retrieve the image file. The image in this file matches the image found in the [`originalImage`](./originalimage.md) key of the dictionary.

## See Also

### Constants
- [static let cropRect: UIImagePickerController.InfoKey](./croprect.md)
  The cropping rectangle that was applied to the original image.
- [static let editedImage: UIImagePickerController.InfoKey](./editedimage.md)
  An image edited by the user.
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
- [static let referenceURL: UIImagePickerController.InfoKey](./referenceurl.md)
  The Assets Library URL for the original version of the picked item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey/imageurl)*