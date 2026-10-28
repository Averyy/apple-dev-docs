# exportSessionWithAsset:presetName:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a new asset export session that uses the specified preset.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) exportSessionWithAsset:(AVAsset *) asset presetName:(NSString *) presetName;
```

## Return Value

An asset export session.

## Parameters

- `asset`: The asset to export.
- `presetName`: A string constant that specifies the preset template for the export. See [Export presets](../export-presets.md) for values an asset export session supports.

## See Also

### Creating an export session
- [init?(asset: AVAsset, presetName: String)](./init%28asset,presetname%29.md)
  Creates an export session with a preset configuration.
- [Export presets](../export-presets.md)
  Configure an export session to output media in standard sizes and formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/exportsessionwithasset:presetname:)*