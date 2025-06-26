# statusUpdates(forAssetPackWithID:)

**Framework**: Background Assets  
**Kind**: method

Gets an asynchronous sequence of download-status updates for the asset pack with the specified ID.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func statusUpdates(forAssetPackWithID assetPackID: String) -> some Sendable & AsyncSequence<AssetPackManager.DownloadStatusUpdate, Never>
```

## Mentions

- [Downloading asset packs hosted by Apple](downloading-asset-packs-hosted-by-apple.md)

#### Return Value

An asynchronous sequence of download-status updates.

#### Discussion

The sequence finishes after yielding [`AssetPackManager.DownloadStatusUpdate.finished(_:)`](assetpackmanager/downloadstatusupdate/finished(_:).md) or [`AssetPackManager.DownloadStatusUpdate.failed(_:_:)`](assetpackmanager/downloadstatusupdate/failed(_:_:).md).

## Parameters

- `assetPackID`: The asset pack’s ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/statusupdates(forassetpackwithid:))*