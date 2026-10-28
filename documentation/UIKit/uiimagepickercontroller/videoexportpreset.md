# videoExportPreset

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The preset to use when preparing video for export to your app.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`PHPickerViewController`](../../PhotosUI/phpickerviewcontroller.md) with [`AVAssetExportSession`](../../AVFoundation/avassetexportsession.md) instead.

## Declaration

```swift
var videoExportPreset: String { get set }
```

```objc
@property (nonatomic, copy) NSString * videoExportPreset;
```

## Discussion

The value of this key is one of the export presets supported by the [`AVAssetExportSession`](../../AVFoundation/avassetexportsession.md) class. For a list of possible values, see the export preset constants in [`AVAssetExportSession`](../../AVFoundation/avassetexportsession.md).

## See Also

### Deprecated
- [var imageExportPreset: UIImagePickerController.ImageURLExportPreset](./imageexportpreset.md)
  The preset to use when preparing images for export to your app.
- [UIImagePickerController.ImageURLExportPreset](./imageurlexportpreset.md)
  Constants that indicate how to export images to the client app.
- [allowsImageEditing](./allowsimageediting.md)
  A Boolean value that indicates whether the user is allowed to edit a selected image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/videoexportpreset)*