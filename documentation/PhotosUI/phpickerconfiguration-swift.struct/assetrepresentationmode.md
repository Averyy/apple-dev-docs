# PHPickerConfiguration.AssetRepresentationMode

**Framework**: PhotosUI  
**Kind**: enum  
**Role**: Enumeration

Constants identifying the mode the system uses when many representations exist for an asset.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS

## Declaration

```swift
enum AssetRepresentationMode
```

## Topics

### Constants
- [PHPickerConfiguration.AssetRepresentationMode.automatic](./assetrepresentationmode/automatic.md)
  The system uses the best representation for the asset.
- [PHPickerConfiguration.AssetRepresentationMode.compatible](./assetrepresentationmode/compatible.md)
  The system uses the most compatible representation if possible.
- [PHPickerConfiguration.AssetRepresentationMode.current](./assetrepresentationmode/current.md)
  The system uses the current representation and avoids transcoding, if possible.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Selecting the preferred asset representation
- [var preferredAssetRepresentationMode: PHPickerConfiguration.AssetRepresentationMode](./preferredassetrepresentationmode.md)
  A mode that determines which representation to use if an asset contains more than one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerconfiguration-swift.struct/assetrepresentationmode)*