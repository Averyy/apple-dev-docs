# mediaMetadata

**Framework**: UIKit  
**Kind**: property

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

#### Discussion

This key is valid only when using an image picker whose source type is set to [`UIImagePickerController.SourceType.camera`](uiimagepickercontroller/sourcetype-swift.enum/camera.md), and applies only to still images.

The value for this key is an [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary) object that contains the metadata of the photo that was just captured. To store the metadata along with the image in the Camera Roll, use the [`PHAssetChangeRequest`](https://developer.apple.com/documentation/Photos/PHAssetChangeRequest) class from the Photos framework.

## See Also

- [static let cropRect: UIImagePickerController.InfoKey](uiimagepickercontroller/infokey/croprect.md)
  The cropping rectangle that was applied to the original image.
- [static let editedImage: UIImagePickerController.InfoKey](uiimagepickercontroller/infokey/editedimage.md)
  An image edited by the user.
- [static let imageURL: UIImagePickerController.InfoKey](uiimagepickercontroller/infokey/imageurl.md)
  The URL of the image file.
- [static let livePhoto: UIImagePickerController.InfoKey](uiimagepickercontroller/infokey/livephoto.md)
  The Live Photo representation of the selected or captured photo.
- [static let mediaType: UIImagePickerController.InfoKey](uiimagepickercontroller/infokey/mediatype.md)
  The media type selected by the user.
- [static let mediaURL: UIImagePickerController.InfoKey](uiimagepickercontroller/infokey/mediaurl.md)
  The filesystem URL for the movie.
- [static let originalImage: UIImagePickerController.InfoKey](uiimagepickercontroller/infokey/originalimage.md)
  The original, uncropped image selected by the user.
- [static let phAsset: UIImagePickerController.InfoKey](uiimagepickercontroller/infokey/phasset.md)
  A Photos asset for the image.
- [static let referenceURL: UIImagePickerController.InfoKey](uiimagepickercontroller/infokey/referenceurl.md)
  The Assets Library URL for the original version of the picked item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey/mediametadata)*