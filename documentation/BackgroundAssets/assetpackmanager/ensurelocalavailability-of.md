# ensureLocalAvailability(of:)

**Framework**: Background Assets  
**Kind**: method

Ensures that the specified asset pack be available locally.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func ensureLocalAvailability(of assetPack: AssetPack) async throws
```

## Mentions

- [Downloading Apple-hosted asset packs](downloading-apple-hosted-asset-packs.md)

#### Discussion

This method checks if the asset pack is currently downloaded. If it isn’t, then it schedules it to be downloaded and waits for the download to complete. It’s guaranteed that the requested asset pack will be available locally once this method returns without throwing. If the method throws, then the asset pack is  guaranteed to be available locally. You can optionally monitor download progress by awaiting status updates from [`statusUpdates`](assetpackmanager/statusupdates.md) or [`statusUpdates(forAssetPackWithID:)`](assetpackmanager/statusupdates(forassetpackwithid:).md) in a different task.

> **Note**: When the asset pack can’t be downloaded.

## Parameters

- `assetPack`: The asset pack the local availability of which to ensure.

## See Also

- [func checkForUpdates() async throws -> (updatingIDs: Set<String>, removedIDs: Set<String>)](assetpackmanager/checkforupdates.md)
  Gets the latest asset-pack information from the server, updates outdated asset packs, and removes obsolete asset packs.
- [func remove(assetPackWithID: String) async throws](assetpackmanager/remove(assetpackwithid:).md)
  Removes the specified asset pack from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/ensurelocalavailability(of:))*