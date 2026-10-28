# ensureLocalAvailability(of:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Ensures that the specified asset pack is available locally, performing a download if necessary.

**Availability**:
- iOS 26.0+ - Deprecated in 26.4 (renamed: ensureLocalAvailability(of:requireLatestVersion:))
- iPadOS 26.0+ - Deprecated in 26.4 (renamed: ensureLocalAvailability(of:requireLatestVersion:))
- Mac Catalyst 26.0+ - Deprecated in 26.4 (renamed: ensureLocalAvailability(of:requireLatestVersion:))
- macOS 26.0+ - Deprecated in 26.4 (renamed: ensureLocalAvailability(of:requireLatestVersion:))
- tvOS 26.0+ - Deprecated in 26.4 (renamed: ensureLocalAvailability(of:requireLatestVersion:))
- visionOS 26.0+ - Deprecated in 26.4 (renamed: ensureLocalAvailability(of:requireLatestVersion:))

## Declaration

```swift
func ensureLocalAvailability(of assetPack: AssetPack) async throws
```

## Mentions

- [Downloading Apple-hosted asset packs](../downloading-apple-hosted-asset-packs.md)

## Discussion

This method checks whether the asset pack is currently downloaded. If it isn’t, then the system schedules it to be downloaded and waits for the download to complete. It’s guaranteed that the requested asset pack will be available locally once this method returns without throwing. If the method throws, then the asset pack *isn’t* guaranteed to be available locally. You can optionally monitor download progress by awaiting status updates from [`statusUpdates`](./statusupdates.md) or [`statusUpdates(forAssetPackWithID:)`](./statusupdates%28forassetpackwithid%29.md) in a separate task.

> **Throws**: When the asset pack can’t be downloaded.

## Parameters

- `assetPack`: The asset pack the local availability of which to ensure.

## See Also

### Managing asset packs
- [func checkForUpdates() async throws -> (updatingIDs: Set<String>, removedIDs: Set<String>)](./checkforupdates%28%29.md)
  Gets the latest asset-pack information from the server, updates outdated asset packs, and removes obsolete asset packs.
- [func ensureLocalAvailability(of: AssetPack, requireLatestVersion: Bool) async throws](./ensurelocalavailability%28of,requirelatestversion%29.md)
  Ensures that an asset pack is available locally, performing a download if necessary.
- [func ensureLocalAvailability(of: Set<AssetPack>, requireLatestVersions: Bool) async throws](./ensurelocalavailability%28of,requirelatestversions%29.md)
  Ensures the specified asset packs are available locally, performing a batch download if necessary.
- [func assetPackIsAvailableLocally(withID: String) -> Bool](./assetpackisavailablelocally%28withid%29.md)
  Checks whether an asset pack is available locally.
- [func status(relativeTo: AssetPack) async throws -> AssetPack.Status](./status%28relativeto%29.md)
  Checks the current status relative to a particular asset pack.
- [func localStatus(ofAssetPackWithID: String) async -> AssetPack.Status](./localstatus%28ofassetpackwithid%29.md)
  Checks an asset pack’s local status.
- [AssetPack.Status](../assetpack/status.md)
  The status of an asset pack.
- [func remove(assetPackWithID: String) async throws](./remove%28assetpackwithid%29.md)
  Removes the specified asset pack from the device.
- [func status(ofAssetPackWithID: String) async throws -> AssetPack.Status](./status%28ofassetpackwithid%29.md)
  Checks an asset pack’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/ensurelocalavailability(of:))*