# status(ofAssetPackWithID:)

**Framework**: Background Assets  
**Kind**: method

Returns an asynchronous sequence of download-status updates for the specified asset pack.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func status(ofAssetPackWithID assetPackID: String) async throws -> AssetPack.Status
```

#### Return Value

The asset pack’s status.

#### Discussion

This method attempts to get the latest asset-pack information from the server. No updates or removals are automatically triggered.

> **Note**: [`ManagedBackgroundAssetsError.assetPackNotFound(withID:)`](managedbackgroundassetserror/assetpacknotfound(withid:).md) when no asset pack with the given ID is found.

## Parameters

- `assetPackID`: The asset pack’s ID.

## See Also

- [let statusUpdates: some Sendable & AsyncSequence<AssetPackManager.DownloadStatusUpdate, Never>](assetpackmanager/statusupdates.md)
  An asynchronous sequence of download-status updates for all asset packs.
- [func statusUpdates(forAssetPackWithID: String) -> some Sendable & AsyncSequence<AssetPackManager.DownloadStatusUpdate, Never>
](assetpackmanager/statusupdates(forassetpackwithid:).md)
  Gets an asynchronous sequence of download-status updates for the asset pack with the specified ID.
- [AssetPackManager.DownloadStatusUpdate](assetpackmanager/downloadstatusupdate.md)
  Statuses of an asset-pack download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/status(ofassetpackwithid:))*