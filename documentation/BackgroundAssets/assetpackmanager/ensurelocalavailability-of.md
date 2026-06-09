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

This method checks whether the asset pack is currently downloaded. If it isn’t, then the system schedules it to be downloaded and waits for the download to complete. It’s guaranteed that the requested asset pack will be available locally once this method returns without throwing. If the method throws, then the asset pack is **not** guaranteed to be available locally. You can optionally monitor download progress by awaiting status updates from [`statusUpdates`](assetpackmanager/statusupdates.md) or [`statusUpdates(forAssetPackWithID:)`](assetpackmanager/statusupdates(forassetpackwithid:).md) in a separate task.

> **Note**: When the asset pack can’t be downloaded.

## Parameters

- `assetPack`: The asset pack the local availability of which to ensure.

## See Also

- [func checkForUpdates() async throws -> (updatingIDs: Set<String>, removedIDs: Set<String>)](assetpackmanager/checkforupdates.md)
  Gets the latest asset-pack information from the server, updates outdated asset packs, and removes obsolete asset packs.
- [func ensureLocalAvailability(of: AssetPack, requireLatestVersion: Bool) async throws](assetpackmanager/ensurelocalavailability(of:requirelatestversion:).md)
  Ensures that an asset pack is available locally, performing a download if necessary.
- [func ensureLocalAvailability(of: Set<AssetPack>, requireLatestVersions: Bool) async throws](assetpackmanager/ensurelocalavailability(of:requirelatestversions:).md)
  Ensures the specified asset packs are available locally, performing a batch download if necessary.
- [func assetPackIsAvailableLocally(withID: String) -> Bool](assetpackmanager/assetpackisavailablelocally(withid:).md)
  Checks whether an asset pack is available locally.
- [func status(relativeTo: AssetPack) async throws -> AssetPack.Status](assetpackmanager/status(relativeto:).md)
  Checks the current status relative to a particular asset pack.
- [func localStatus(ofAssetPackWithID: String) async -> AssetPack.Status](assetpackmanager/localstatus(ofassetpackwithid:).md)
  Checks an asset pack’s local status.
- [AssetPack.Status](assetpack/status.md)
  The status of an asset pack.
- [func remove(assetPackWithID: String) async throws](assetpackmanager/remove(assetpackwithid:).md)
  Removes the specified asset pack from the device.
- [func status(ofAssetPackWithID: String) async throws -> AssetPack.Status](assetpackmanager/status(ofassetpackwithid:).md)
  Checks an asset pack’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/ensurelocalavailability(of:))*