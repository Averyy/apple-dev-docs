# videoExportPreset

**Framework**: UIKit  
**Kind**: property

The preset to use when preparing video for export to your app.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var videoExportPreset: String { get set }
```

#### Discussion

The value of this key is one of the export presets supported by the [`AVAssetExportSession`](https://developer.apple.com/documentation/AVFoundation/AVAssetExportSession) class. For a list of possible values, see the export preset constants in [`AVAssetExportSession`](https://developer.apple.com/documentation/AVFoundation/AVAssetExportSession).

## See Also

- [var imageExportPreset: UIImagePickerController.ImageURLExportPreset](uiimagepickercontroller/imageexportpreset.md)
  The preset to use when preparing images for export to your app.
- [UIImagePickerController.ImageURLExportPreset](uiimagepickercontroller/imageurlexportpreset.md)
  Constants that indicate how to export images to the client app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/videoexportpreset)*