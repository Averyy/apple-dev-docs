# statusUpdates

**Framework**: Background Assets  
**Kind**: property

An asynchronous sequence of download-status updates for all asset packs.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final let statusUpdates: some Sendable & AsyncSequence<AssetPackManager.DownloadStatusUpdate, Never>
```

#### Discussion

The sequence never finishes.

## See Also

- [func statusUpdates(forAssetPackWithID: String) -> some Sendable & AsyncSequence<AssetPackManager.DownloadStatusUpdate, Never>
](assetpackmanager/statusupdates(forassetpackwithid:).md)
  Gets an asynchronous sequence of download-status updates for the asset pack with the specified ID.
- [AssetPackManager.DownloadStatusUpdate](assetpackmanager/downloadstatusupdate.md)
  Statuses of an asset-pack download.
- [func status(ofAssetPackWithID: String) async throws -> AssetPack.Status](assetpackmanager/status(ofassetpackwithid:).md)
  Returns an asynchronous sequence of download-status updates for the specified asset pack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/statusupdates)*