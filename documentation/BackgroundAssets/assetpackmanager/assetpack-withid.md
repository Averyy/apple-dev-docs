# assetPack(withID:)

**Framework**: Background Assets  
**Kind**: method

Returns the asset pack with the given ID.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func assetPack(withID id: String) async throws -> AssetPack
```

## Mentions

- [Downloading Apple-hosted asset packs](downloading-apple-hosted-asset-packs.md)

#### Return Value

The asset pack.

#### Discussion

This method may attempt to get the latest asset-pack information from the server if the system hasn’t cached that information locally. To force the system to get the latest information from the server unconditionally, call [`checkForUpdates()`](assetpackmanager/checkforupdates().md).

> **Note**: [`ManagedBackgroundAssetsError.assetPackNotFound(withID:)`](managedbackgroundassetserror/assetpacknotfound(withid:).md) when no asset pack with the given ID is found.

## Parameters

- `id`: The asset pack’s ID.

## See Also

- [var manifest: AssetPackManifest](assetpackmanager/manifest.md)
  The manifest of asset packs that are available to download.
- [struct AssetPackManifest](assetpackmanifest.md)
  A manifest of asset packs that are available to download.
- [var allAssetPacks: Set<AssetPack>](assetpackmanager/allassetpacks.md)
  The asset packs that are available to download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/assetpack(withid:))*