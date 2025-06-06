# determineCompatibleFileTypes(completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Determines the output file types an asset export session supports writing in its current configuration.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var compatibleFileTypes: [AVFileType] { get async }
```

## Parameters

- `handler`: A callback the system passes an array of   structures when it determines the compatible file types.

## See Also

- [var presetName: String](avassetexportsession/presetname.md)
  The name of the preset that the asset export session uses.
- [class func allExportPresets() -> [String]](avassetexportsession/allexportpresets.md)
  Returns all available export preset names.
- [class func determineCompatibility(ofExportPreset: String, with: AVAsset, outputFileType: AVFileType?, completionHandler: (Bool) -> Void)](avassetexportsession/determinecompatibility(ofexportpreset:with:outputfiletype:completionhandler:).md)
  Determines an export preset’s compatibility to export the asset in a container of the output file type.
- [class func exportPresets(compatibleWith: AVAsset) -> [String]](avassetexportsession/exportpresets(compatiblewith:).md)
  Returns compatible export presets for the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/determinecompatiblefiletypes(completionhandler:))*