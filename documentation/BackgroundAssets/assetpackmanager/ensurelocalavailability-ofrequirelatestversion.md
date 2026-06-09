# ensureLocalAvailability(of:requireLatestVersion:)

**Framework**: Background Assets  
**Kind**: method

Ensures that an asset pack is available locally, performing a download if necessary.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+

## Declaration

```swift
func ensureLocalAvailability(of assetPack: AssetPack, requireLatestVersion shouldUpdate: Bool = false) async throws
```

## Mentions

- [Reducing download and storage demands with localized asset packs](reducing-download-and-storage-demands-with-localized-asset-packs.md)

#### Discussion

This method checks whether the asset pack is currently downloaded. If it isn’t, then the system schedules it to be downloaded and waits for the download to finish. If the method returns without throwing, the framework guarantees that the requested asset pack is now available locally. If the method throws, then the asset pack *isn’t* guaranteed to be available locally. You can optionally monitor download progress by awaiting status updates from [`statusUpdates`](assetpackmanager/statusupdates.md) or [`statusUpdates(forAssetPackWithID:)`](assetpackmanager/statusupdates(forassetpackwithid:).md) in a separate task.

To download multiple asset packs at the same time, use [`ensureLocalAvailability(of:requireLatestVersions:)`](assetpackmanager/ensurelocalavailability(of:requirelatestversions:).md).

> **Note**:  When the system can’t ensure the asset pack’s local availability.

## Parameters

- `assetPack`: The asset pack the local availability of which to ensure.
- `shouldUpdate`: Whether to require that the latest version be available locally. When `true` is passed to this parameter, the method will wait for the update (if there indeed is one available) to be downloaded before returning. When `false` is passed, the method won’t check for updates and won’t attempt to download any.

## See Also

- [func checkForUpdates() async throws -> (updatingIDs: Set<String>, removedIDs: Set<String>)](assetpackmanager/checkforupdates.md)
  Gets the latest asset-pack information from the server, updates outdated asset packs, and removes obsolete asset packs.
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
- [func ensureLocalAvailability(of: AssetPack) async throws](assetpackmanager/ensurelocalavailability(of:).md)
  Ensures that the specified asset pack be available locally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/ensurelocalavailability(of:requirelatestversion:))*