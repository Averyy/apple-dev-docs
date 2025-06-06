# determineCompatibility(ofExportPreset:with:outputFileType:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Determines an export preset’s compatibility to export the asset in a container of the output file type.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func compatibility(ofExportPreset presetName: String, with asset: AVAsset, outputFileType: AVFileType?) async -> Bool
```

## Parameters

- `presetName`: The name of the preset whose compatibility you want to test. See   for preset values an asset export session supports.
- `asset`: The asset to export.
- `outputFileType`: The file type of the output container.
- `handler`: A callback the system passes a Boolean result when it determines the compatibility of the preset.

## See Also

- [var presetName: String](avassetexportsession/presetname.md)
  The name of the preset that the asset export session uses.
- [func determineCompatibleFileTypes(completionHandler: ([AVFileType]) -> Void)](avassetexportsession/determinecompatiblefiletypes(completionhandler:).md)
  Determines the output file types an asset export session supports writing in its current configuration.
- [class func allExportPresets() -> [String]](avassetexportsession/allexportpresets.md)
  Returns all available export preset names.
- [class func exportPresets(compatibleWith: AVAsset) -> [String]](avassetexportsession/exportpresets(compatiblewith:).md)
  Returns compatible export presets for the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/determinecompatibility(ofexportpreset:with:outputfiletype:completionhandler:))*