# allowsImageEditing

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the user is allowed to edit a selected image.

**Availability**:
- iOS 2.0+ - Deprecated in 3.1
- iPadOS 2.0+ - Deprecated in 3.1
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`allowsEditing`](./allowsediting.md) instead.

## Declaration

```objc
@property (nonatomic) BOOL allowsImageEditing;
```

#### Discussion

If you allow the user to edit images, the delegate may receive a dictionary with information about the edits that were made.

This property is set to [`false`](../../Swift/false.md) by default.

## See Also

### Deprecated
- [var imageExportPreset: UIImagePickerController.ImageURLExportPreset](./imageexportpreset.md)
  The preset to use when preparing images for export to your app.
- [UIImagePickerController.ImageURLExportPreset](./imageurlexportpreset.md)
  Constants that indicate how to export images to the client app.
- [var videoExportPreset: String](./videoexportpreset.md)
  The preset to use when preparing video for export to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/allowsimageediting)*