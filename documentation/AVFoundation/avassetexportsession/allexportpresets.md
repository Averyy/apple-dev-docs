# allExportPresets()

**Framework**: AVFoundation  
**Kind**: method

Returns all available export preset names.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func allExportPresets() -> [String]
```

#### Return Value

See [`Export presets`](export-presets.md) for values an asset export session supports.

#### Discussion

Not all presets are compatible with all assets.

## See Also

- [var presetName: String](avassetexportsession/presetname.md)
  The name of the preset that the asset export session uses.
- [func determineCompatibleFileTypes(completionHandler: ([AVFileType]) -> Void)](avassetexportsession/determinecompatiblefiletypes(completionhandler:).md)
  Determines the output file types an asset export session supports writing in its current configuration.
- [class func determineCompatibility(ofExportPreset: String, with: AVAsset, outputFileType: AVFileType?, completionHandler: (Bool) -> Void)](avassetexportsession/determinecompatibility(ofexportpreset:with:outputfiletype:completionhandler:).md)
  Determines an export preset’s compatibility to export the asset in a container of the output file type.
- [class func exportPresets(compatibleWith: AVAsset) -> [String]](avassetexportsession/exportpresets(compatiblewith:).md)
  Returns compatible export presets for the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/allexportpresets())*