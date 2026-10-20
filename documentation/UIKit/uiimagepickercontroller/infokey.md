# UIImagePickerController.InfoKey

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Keys you use to retrieve information from the editing dictionary about the media that the user selected.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
struct InfoKey
```

```c
typedef NSString * UIImagePickerControllerInfoKey;
```

## Topics

### Constants
- [static let cropRect: UIImagePickerController.InfoKey](./infokey/croprect.md)
  The cropping rectangle that was applied to the original image.
- [static let editedImage: UIImagePickerController.InfoKey](./infokey/editedimage.md)
  An image edited by the user.
- [static let imageURL: UIImagePickerController.InfoKey](./infokey/imageurl.md)
  The URL of the image file.
- [static let livePhoto: UIImagePickerController.InfoKey](./infokey/livephoto.md)
  The Live Photo representation of the selected or captured photo.
- [static let mediaMetadata: UIImagePickerController.InfoKey](./infokey/mediametadata.md)
  Metadata for a newly-captured photograph.
- [static let mediaType: UIImagePickerController.InfoKey](./infokey/mediatype.md)
  The media type selected by the user.
- [static let mediaURL: UIImagePickerController.InfoKey](./infokey/mediaurl.md)
  The filesystem URL for the movie.
- [static let originalImage: UIImagePickerController.InfoKey](./infokey/originalimage.md)
  The original, uncropped image selected by the user.
- [static let phAsset: UIImagePickerController.InfoKey](./infokey/phasset.md)
  A Photos asset for the image.
- [static let referenceURL: UIImagePickerController.InfoKey](./infokey/referenceurl.md)
  The Assets Library URL for the original version of the picked item.
### Initializers
- [init(rawValue: String)](./infokey/init%28rawvalue%29.md)
  Creates a new editing information key with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey)*