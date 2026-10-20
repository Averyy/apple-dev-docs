# cropRect

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The cropping rectangle that was applied to the original image.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
static let cropRect: UIImagePickerController.InfoKey
```

```c
extern UIImagePickerControllerInfoKey const UIImagePickerControllerCropRect;
```

#### Discussion

The value for this key is an [`NSValue`](../../../Foundation/nsvalue.md) object containing a [`CGRect`](../../../CoreFoundation/cgrect.md) opaque type.

## See Also

### Constants
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
- [static let referenceURL: UIImagePickerController.InfoKey](./referenceurl.md)
  The Assets Library URL for the original version of the picked item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey/croprect)*