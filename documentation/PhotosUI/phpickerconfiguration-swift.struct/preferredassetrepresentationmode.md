# preferredAssetRepresentationMode

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

A mode that determines which representation to use if an asset contains more than one.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS

## Declaration

```swift
var preferredAssetRepresentationMode: PHPickerConfiguration.AssetRepresentationMode
```

#### Discussion

An asset can contain many representations under the same uniform type identifier, or you can prefer a specific format. This mode determines which representation an [`NSItemProvider`](../../Foundation/nsitemprovider.md) uses if many exist.

The system may perform additional transcoding to convert the asset you request to the compatable representation. Use [`PHPickerConfiguration.AssetRepresentationMode.current`](./assetrepresentationmode/current.md) to avoid transcoding, if possible.

## See Also

### Selecting the preferred asset representation
- [PHPickerConfiguration.AssetRepresentationMode](./assetrepresentationmode.md)
  Constants identifying the mode the system uses when many representations exist for an asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerconfiguration-swift.struct/preferredassetrepresentationmode)*