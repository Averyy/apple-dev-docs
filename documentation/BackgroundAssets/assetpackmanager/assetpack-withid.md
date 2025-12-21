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
func assetPack(withID assetPackID: String) async throws -> AssetPack
```

## Mentions

- [Downloading Apple-hosted asset packs](downloading-apple-hosted-asset-packs.md)

#### Return Value

The asset pack.

#### Discussion

This method might attempt to get the latest asset-pack information from the server.

> **Note**: [`ManagedBackgroundAssetsError.assetPackNotFound(withID:)`](managedbackgroundassetserror/assetpacknotfound(withid:).md) when no asset pack with the given ID is found.

## Parameters

- `assetPackID`: The asset pack’s ID.

## See Also

- [var allAssetPacks: Set<AssetPack>](assetpackmanager/allassetpacks.md)
  The asset packs that are available to download.
- [func contents(at: FilePath, searchingInAssetPackWithID: String?, options: Data.ReadingOptions) throws -> Data](assetpackmanager/contents(at:searchinginassetpackwithid:options:).md)
  Returns the contents of an asset file at the specified relative path.
- [func descriptor(for: FilePath, searchingInAssetPackWithID: String?) throws -> FileDescriptor](assetpackmanager/descriptor(for:searchinginassetpackwithid:).md)
  Opens and returns a file descriptor for an asset file at the specified relative path.
- [func url(for: FilePath) throws -> URL](assetpackmanager/url(for:).md)
  Returns a URL for the specified relative path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/assetpack(withid:))*