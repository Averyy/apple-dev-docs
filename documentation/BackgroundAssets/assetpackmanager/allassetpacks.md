# allAssetPacks

**Framework**: Background Assets  
**Kind**: property  
**Role**: Instance Property

The asset packs that are available to download.

**Availability**:
- iOS 26.0+ - Deprecated in 27.0
- iPadOS 26.0+ - Deprecated in 27.0
- Mac Catalyst 26.0+ - Deprecated in 27.0
- macOS 26.0+ - Deprecated in 27.0
- tvOS 26.0+ - Deprecated in 27.0
- visionOS 26.0+ - Deprecated in 27.0

> **Deprecated**: Use the manager’s manifest property’s value’s assetPacks property.

## Declaration

```swift
var allAssetPacks: Set<AssetPack> { get async throws }
```

#### Discussion

Accessing this property may cause an attempt to get the latest asset-pack information from the server.

## See Also

### Accessing asset packs
- [var manifest: AssetPackManifest](./manifest.md)
  The manifest of asset packs that are available to download.
- [struct AssetPackManifest](../assetpackmanifest.md)
  A manifest of asset packs that are available to download.
- [func assetPack(withID: String) async throws -> AssetPack](./assetpack%28withid%29.md)
  Returns the asset pack with the given ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/allassetpacks)*