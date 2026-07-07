# ensureLocalAvailability(of:requireLatestVersions:)

**Framework**: Background Assets  
**Kind**: method

Ensures the specified asset packs are available locally, performing a batch download if necessary.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func ensureLocalAvailability(of assetPacks: Set<AssetPack>, requireLatestVersions shouldUpdate: Bool = false) async throws
```

## Mentions

- [Reducing download and storage demands with localized asset packs](reducing-download-and-storage-demands-with-localized-asset-packs.md)

#### Discussion

This method checks whether the asset packs are currently downloaded. If any aren’t, then the system schedules them to be downloaded and waits for all of the downloads to finish. The framework guarantees that the requested asset packs are available locally after this method returns without throwing. If the method throws, then the asset packs *aren’t* all guaranteed to be available locally, though some might be; inspect the thrown error for more details. You can optionally monitor download progress by awaiting status updates from [`statusUpdates`](assetpackmanager/statusupdates.md) or [`statusUpdates(forAssetPackWithID:)`](assetpackmanager/statusupdates(forassetpackwithid:).md) in a separate task.

> **Note**:  When the system can’t ensure one or more asset packs’ local availability. When the thrown error is an instance of [`AssetPackManager.LocalAvailabilityError`](assetpackmanager/localavailabilityerror.md), it provides information about asset packs for which the system successfully ensured local availability and those for which the system couldn’t ensure local availability, with an underlying error for each failure.

## Parameters

- `assetPacks`: The asset packs the local availability of which to ensure.
- `shouldUpdate`: Whether to require that the respective latest versions be available locally. When `true` is passed to this parameter, the method will wait for the updates (if there indeed are any available) to be downloaded before returning. When `false` is passed, the method won’t check for updates and won’t attempt to download any.

## See Also

- [func checkForUpdates() async throws -> (updatingIDs: Set<String>, removedIDs: Set<String>)](assetpackmanager/checkforupdates.md)
  Gets the latest asset-pack information from the server, updates outdated asset packs, and removes obsolete asset packs.
- [func ensureLocalAvailability(of: AssetPack, requireLatestVersion: Bool) async throws](assetpackmanager/ensurelocalavailability(of:requirelatestversion:).md)
  Ensures that an asset pack is available locally, performing a download if necessary.
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
- [func ensureLocalAvailability(of: AssetPack) async throws](assetpackmanager/ensurelocalavailability(of:).md)
  Ensures that the specified asset pack is available locally, performing a download if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/ensurelocalavailability(of:requirelatestversions:))*