# statusUpdates(forAssetPackWithID:)

**Framework**: Background Assets  
**Kind**: method

Gets an asynchronous sequence of download-status updates for the asset pack with the specified ID.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
func statusUpdates(forAssetPackWithID assetPackID: String) -> some Sendable & AsyncSequence<AssetPackManager.DownloadStatusUpdate, Never>
```

## Mentions

- [Downloading Apple-hosted asset packs](downloading-apple-hosted-asset-packs.md)

#### Return Value

An asynchronous sequence of download-status updates.

#### Discussion

The sequence finishes after yielding [`AssetPackManager.DownloadStatusUpdate.finished(_:)`](assetpackmanager/downloadstatusupdate/finished(_:).md) or [`AssetPackManager.DownloadStatusUpdate.failed(_:_:)`](assetpackmanager/downloadstatusupdate/failed(_:_:).md).

## Parameters

- `assetPackID`: The asset pack’s ID.

## See Also

- [let statusUpdates: some Sendable & AsyncSequence<AssetPackManager.DownloadStatusUpdate, Never>](assetpackmanager/statusupdates.md)
  An asynchronous sequence of download-status updates for all asset packs.
- [AssetPackManager.DownloadStatusUpdate](assetpackmanager/downloadstatusupdate.md)
  Statuses of an asset-pack download.
- [func status(ofAssetPackWithID: String) async throws -> AssetPack.Status](assetpackmanager/status(ofassetpackwithid:).md)
  Returns an asynchronous sequence of download-status updates for the specified asset pack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/statusupdates(forassetpackwithid:))*