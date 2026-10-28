# imageExportPreset

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The preset to use when preparing images for export to your app.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`PHPickerViewController`](../../PhotosUI/phpickerviewcontroller.md) instead.

## Declaration

```swift
var imageExportPreset: UIImagePickerController.ImageURLExportPreset { get set }
```

```objc
@property (nonatomic) UIImagePickerControllerImageURLExportPreset imageExportPreset;
```

## Discussion

The default value of this property is [`UIImagePickerController.ImageURLExportPreset.compatible`](./imageurlexportpreset/compatible.md).

## See Also

### Deprecated
- [UIImagePickerController.ImageURLExportPreset](./imageurlexportpreset.md)
  Constants that indicate how to export images to the client app.
- [var videoExportPreset: String](./videoexportpreset.md)
  The preset to use when preparing video for export to your app.
- [allowsImageEditing](./allowsimageediting.md)
  A Boolean value that indicates whether the user is allowed to edit a selected image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/imageexportpreset)*