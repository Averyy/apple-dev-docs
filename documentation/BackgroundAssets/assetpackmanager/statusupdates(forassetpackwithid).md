# statusUpdates(forAssetPackWithID:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Returns an asynchronous sequence of download-status updates for the asset pack with the specified ID.

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

- [Downloading Apple-hosted asset packs](../downloading-apple-hosted-asset-packs.md)
- [Reducing download and storage demands with localized asset packs](../reducing-download-and-storage-demands-with-localized-asset-packs.md)

#### Return Value

An asynchronous sequence of download-status updates.

#### Discussion

The sequence finishes after yielding [`AssetPackManager.DownloadStatusUpdate.finished(_:)`](./downloadstatusupdate/finished%28_%29.md) or [`AssetPackManager.DownloadStatusUpdate.failed(_:_:)`](./downloadstatusupdate/failed%28_,_%29.md).

## Parameters

- `assetPackID`: The asset pack’s ID.

## See Also

### Tracking downloads
- [let statusUpdates: some Sendable & AsyncSequence<AssetPackManager.DownloadStatusUpdate, Never>](./statusupdates.md)
  An asynchronous sequence of download-status updates for all asset packs.
- [AssetPackManager.DownloadStatusUpdate](./downloadstatusupdate.md)
  Statuses of an asset-pack download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/statusupdates(forassetpackwithid:))*