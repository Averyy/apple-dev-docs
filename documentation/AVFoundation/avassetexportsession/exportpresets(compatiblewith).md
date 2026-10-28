# exportPresets(compatibleWith:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns compatible export presets for the asset.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0

> **Deprecated**: Use [`determineCompatibility(ofExportPreset:with:outputFileType:completionHandler:)`](./determinecompatibility%28ofexportpreset,with,outputfiletype,completionhandler%29.md) instead.

## Declaration

```swift
class func exportPresets(compatibleWith asset: AVAsset) -> [String]
```

```objc
+ (NSArray<NSString *> *) exportPresetsCompatibleWithAsset:(AVAsset *) asset;
```

## Return Value

An array of compatible presets. See [Export presets](../export-presets.md) for preset values an asset export session supports.

## Discussion

Not all export presets are compatible with all assets. For example, video-only assets aren’t compatible with an audio-only preset. Call this method to determine the compatible presets for the asset you’re exporting.

> ❗ **Important**:  Load the asset’s [`tracks`](../avasset/tracks.md) property before calling this method to avoid blocking the calling thread.

## Parameters

- `asset`: An asset to export.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/exportpresets(compatiblewith:))*