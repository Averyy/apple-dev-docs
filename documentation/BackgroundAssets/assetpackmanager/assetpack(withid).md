# assetPack(withID:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Returns the asset pack with the given ID.

**Availability**:
- iOS 26.0+ - Deprecated in 27.0
- iPadOS 26.0+ - Deprecated in 27.0
- Mac Catalyst 26.0+ - Deprecated in 27.0
- macOS 26.0+ - Deprecated in 27.0
- tvOS 26.0+ - Deprecated in 27.0
- visionOS 26.0+ - Deprecated in 27.0

> **Deprecated**: Call assetPack(withID:) on the manager’s manifest property’s value.

## Declaration

```swift
func assetPack(withID id: String) async throws -> AssetPack
```

## Mentions

- [Downloading Apple-hosted asset packs](../downloading-apple-hosted-asset-packs.md)

## Return Value

The asset pack.

## Discussion

This method may attempt to get the latest asset-pack information from the server if the system hasn’t cached that information locally. To force the system to get the latest information from the server unconditionally, call [`checkForUpdates()`](./checkforupdates%28%29.md).

> **Throws**: [`ManagedBackgroundAssetsError.assetPackNotFound(withID:)`](../managedbackgroundassetserror/assetpacknotfound%28withid%29.md) when no asset pack with the given ID is found.

## Parameters

- `id`: The asset pack’s ID.

## See Also

### Accessing asset packs
- [var manifest: AssetPackManifest](./manifest.md)
  The manifest of asset packs that are available to download.
- [struct AssetPackManifest](../assetpackmanifest.md)
  A manifest of asset packs that are available to download.
- [var allAssetPacks: Set<AssetPack>](./allassetpacks.md)
  The asset packs that are available to download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/assetpack(withid:))*