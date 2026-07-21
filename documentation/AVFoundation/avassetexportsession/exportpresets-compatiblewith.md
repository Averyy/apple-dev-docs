# exportPresets(compatibleWith:)

**Framework**: AVFoundation  
**Kind**: method

Returns compatible export presets for the asset.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+

## Declaration

```swift
class func exportPresets(compatibleWith asset: AVAsset) -> [String]
```

#### Return Value

An array of compatible presets. See [`Export presets`](export-presets.md) for preset values an asset export session supports.

#### Discussion

Not all export presets are compatible with all assets. For example, video-only assets aren’t compatible with an audio-only preset. Call this method to determine the compatible presets for the asset you’re exporting.

> ❗ **Important**:  Load the asset’s [`tracks`](avasset/tracks.md) property before calling this method to avoid blocking the calling thread.

## Parameters

- `asset`: An asset to export.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/exportpresets(compatiblewith:))*