# livePhoto

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

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

```c
extern UIImagePickerControllerInfoKey const UIImagePickerControllerLivePhoto;
```

#### Discussion

A Live Photo is a picture, that includes motion and sound from the moments just before and after its capture. On compatible devices, the Camera app captures all photos as Live Photos by default, but the [`imagePickerController:didFinishPickingImage:editingInfo:`](../../uiimagepickercontrollerdelegate/imagepickercontroller_didfinishpickingimage_editinginfo_.md) method’s `image` parameter contains only the still image representation.

To obtain the motion and sound content of a live photo for display (using the [`PHLivePhotoView`](../../../PhotosUI/phlivephotoview.md) class), include the `kUTTypeImage` and `kUTTypeLivePhoto` identifiers in the allowed media types when configuring an image picker controller. When the user picks or captures a Live Photo, the `editingInfo` dictionary contains the [`livePhoto`](./livephoto.md) key, with a [`PHLivePhoto`](../../../Photos/phlivephoto.md) representation of the photo as the corresponding value.

## See Also

### Constants
- [static let cropRect: UIImagePickerController.InfoKey](./croprect.md)
  The cropping rectangle that was applied to the original image.
- [static let editedImage: UIImagePickerController.InfoKey](./editedimage.md)
  An image edited by the user.
- [static let imageURL: UIImagePickerController.InfoKey](./imageurl.md)
  The URL of the image file.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey/livephoto)*