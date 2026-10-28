# allExportPresets()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSArray<NSString *> *) allExportPresets;
```

## Return Value

See [Export presets](../export-presets.md) for values an asset export session supports.

## Discussion

Not all presets are compatible with all assets.

## See Also

### Accessing export presets
- [var presetName: String](./presetname.md)
  The name of the preset that the asset export session uses.
- [func determineCompatibleFileTypes(completionHandler: ([AVFileType]) -> Void)](./determinecompatiblefiletypes%28completionhandler%29.md)
  Determines the output file types an asset export session supports writing in its current configuration.
- [class func determineCompatibility(ofExportPreset: String, with: AVAsset, outputFileType: AVFileType?, completionHandler: (Bool) -> Void)](./determinecompatibility%28ofexportpreset,with,outputfiletype,completionhandler%29.md)
  Determines an export preset’s compatibility to export the asset in a container of the output file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/allexportpresets())*