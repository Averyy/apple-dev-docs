# UIImagePickerController.InfoKey

**Framework**: UIKit  
**Kind**: struct

Keys you use to retrieve information from the editing dictionary about the media that the user selected.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
struct InfoKey
```

## Topics

### Constants
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
- [static let referenceURL: UIImagePickerController.InfoKey](uiimagepickercontroller/infokey/referenceurl.md)
  The Assets Library URL for the original version of the picked item.
### Initializers
- [init(rawValue: String)](uiimagepickercontroller/infokey/init(rawvalue:).md)
  Creates a new editing information key with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey)*