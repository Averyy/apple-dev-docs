# imageURL

**Framework**: UIKit  
**Kind**: property

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

#### Discussion

The value of this key is a [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) that you can use to retrieve the image file. The image in this file matches the image found in the [`originalImage`](uiimagepickercontroller/infokey/originalimage.md) key of the dictionary.

## See Also

- [static let cropRect: UIImagePickerController.InfoKey](uiimagepickercontroller/infokey/croprect.md)
  The cropping rectangle that was applied to the original image.
- [static let editedImage: UIImagePickerController.InfoKey](uiimagepickercontroller/infokey/editedimage.md)
  An image edited by the user.
- [static let livePhoto: UIImagePickerController.InfoKey](uiimagepickercontroller/infokey/livephoto.md)
  The Live Photo representation of the selected or captured photo.
- [static let mediaMetadata: UIImagePickerController.InfoKey](uiimagepickercontroller/infokey/mediametadata.md)
  Metadata for a newly-captured photograph.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey/imageurl)*