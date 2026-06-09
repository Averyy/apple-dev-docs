# manifest

**Framework**: Background Assets  
**Kind**: property

The manifest of asset packs that are available to download.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var manifest: AssetPackManifest { get async throws }
```

## Mentions

- [Reducing download and storage demands with localized asset packs](reducing-download-and-storage-demands-with-localized-asset-packs.md)

## See Also

- [struct AssetPackManifest](assetpackmanifest.md)
  A manifest of asset packs that are available to download.
- [var allAssetPacks: Set<AssetPack>](assetpackmanager/allassetpacks.md)
  The asset packs that are available to download.
- [func assetPack(withID: String) async throws -> AssetPack](assetpackmanager/assetpack(withid:).md)
  Returns the asset pack with the given ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/manifest)*