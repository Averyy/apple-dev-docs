# referenceURL

**Framework**: UIKit  
**Kind**: property

The Assets Library URL for the original version of the picked item.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+

## Declaration

```swift
static let referenceURL: UIImagePickerController.InfoKey
```

#### Discussion

After the user edits a picked item—such as by cropping an image or trimming a movie—the URL continues to point to the original version of the picked item.

The value for this key is an [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) object.

## See Also

- [static let cropRect: UIImagePickerController.InfoKey](uiimagepickercontroller/infokey/croprect.md)
  The cropping rectangle that was applied to the original image.
- [static let editedImage: UIImagePickerController.InfoKey](uiimagepickercontroller/infokey/editedimage.md)
  An image edited by the user.
- [static let imageURL: UIImagePickerController.InfoKey](uiimagepickercontroller/infokey/imageurl.md)
  The URL of the image file.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey/referenceurl)*