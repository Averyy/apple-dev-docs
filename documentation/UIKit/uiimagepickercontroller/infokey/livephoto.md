# livePhoto

**Framework**: UIKit  
**Kind**: property

The Live Photo representation of the selected or captured photo.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
static let livePhoto: UIImagePickerController.InfoKey
```

#### Discussion

A Live Photo is a picture, that includes motion and sound from the moments just before and after its capture. On compatible devices, the Camera app captures all photos as Live Photos by default, but the [`imagePickerController:didFinishPickingImage:editingInfo:`](uiimagepickercontrollerdelegate/imagepickercontroller:didfinishpickingimage:editinginfo:.md) method’s `image` parameter contains only the still image representation.

To obtain the motion and sound content of a live photo for display (using the [`PHLivePhotoView`](https://developer.apple.com/documentation/PhotosUI/PHLivePhotoView) class), include the `kUTTypeImage` and `kUTTypeLivePhoto` identifiers in the allowed media types when configuring an image picker controller. When the user picks or captures a Live Photo, the `editingInfo` dictionary contains the [`livePhoto`](uiimagepickercontroller/infokey/livephoto.md) key, with a [`PHLivePhoto`](https://developer.apple.com/documentation/Photos/PHLivePhoto) representation of the photo as the corresponding value.

## See Also

- [static let cropRect: UIImagePickerController.InfoKey](uiimagepickercontroller/infokey/croprect.md)
  The cropping rectangle that was applied to the original image.
- [static let editedImage: UIImagePickerController.InfoKey](uiimagepickercontroller/infokey/editedimage.md)
  An image edited by the user.
- [static let imageURL: UIImagePickerController.InfoKey](uiimagepickercontroller/infokey/imageurl.md)
  The URL of the image file.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey/livephoto)*