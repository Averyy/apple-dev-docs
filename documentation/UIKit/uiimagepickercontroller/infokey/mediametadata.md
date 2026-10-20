# mediaMetadata

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

Metadata for a newly-captured photograph.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
static let mediaMetadata: UIImagePickerController.InfoKey
```

```c
extern UIImagePickerControllerInfoKey const UIImagePickerControllerMediaMetadata;
```

#### Discussion

This key is valid only when using an image picker whose source type is set to [`UIImagePickerController.SourceType.camera`](../sourcetype-swift.enum/camera.md), and applies only to still images.

The value for this key is an [`NSDictionary`](../../../Foundation/nsdictionary.md) object that contains the metadata of the photo that was just captured. To store the metadata along with the image in the Camera Roll, use the [`PHAssetChangeRequest`](https://developer.apple.com/documentation/photos/phassetchangerequest) class from the Photos framework.

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey/mediametadata)*