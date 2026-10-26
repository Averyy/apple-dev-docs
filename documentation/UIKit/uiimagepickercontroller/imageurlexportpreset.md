# UIImagePickerController.ImageURLExportPreset

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate how to export images to the client app.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`PHPickerViewController`](../../PhotosUI/phpickerviewcontroller.md) instead.

## Declaration

```swift
enum ImageURLExportPreset
```

```c
enum UIImagePickerControllerImageURLExportPreset : NSInteger;
```

## Topics

### Constants
- [UIImagePickerController.ImageURLExportPreset.compatible](./imageurlexportpreset/compatible.md)
  A preset for converting HEIF formatted images to JPEG.
- [UIImagePickerController.ImageURLExportPreset.current](./imageurlexportpreset/current.md)
  A preset for passing image data as-is to the client.
### Initializers
- [init?(rawValue: Int)](./imageurlexportpreset/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Deprecated
- [var imageExportPreset: UIImagePickerController.ImageURLExportPreset](./imageexportpreset.md)
  The preset to use when preparing images for export to your app.
- [var videoExportPreset: String](./videoexportpreset.md)
  The preset to use when preparing video for export to your app.
- [allowsImageEditing](./allowsimageediting.md)
  A Boolean value that indicates whether the user is allowed to edit a selected image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/imageurlexportpreset)*