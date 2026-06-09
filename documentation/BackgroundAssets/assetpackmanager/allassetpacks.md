# allAssetPacks

**Framework**: Background Assets  
**Kind**: property

The asset packs that are available to download.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var allAssetPacks: Set<AssetPack> { get async throws }
```

#### Discussion

Accessing this property may cause an attempt to get the latest asset-pack information from the server.

## See Also

- [var manifest: AssetPackManifest](assetpackmanager/manifest.md)
  The manifest of asset packs that are available to download.
- [struct AssetPackManifest](assetpackmanifest.md)
  A manifest of asset packs that are available to download.
- [func assetPack(withID: String) async throws -> AssetPack](assetpackmanager/assetpack(withid:).md)
  Returns the asset pack with the given ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/allassetpacks)*