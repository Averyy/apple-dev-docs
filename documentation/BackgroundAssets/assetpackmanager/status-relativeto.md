# status(relativeTo:)

**Framework**: Background Assets  
**Kind**: method

Checks the current status relative to a particular asset pack.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+

## Declaration

```swift
func status(relativeTo assetPack: AssetPack) async throws -> AssetPack.Status
```

#### Return Value

The current status relative to the asset pack.

#### Discussion

This method checks whether any version of the specified asset pack is currently downloaded. If one is, then it determines the version relationship between the downloaded asset pack and the specified asset pack. If they have different version numbers, then the returned status value will contain [`outOfDate`](assetpack/status/outofdate.md). The returned status value will contain [`updateAvailable`](assetpack/status/updateavailable.md) only if the relevant asset pack on the server hasn’t been further updated since the initialization of the provided [`AssetPack`](assetpack.md) instance.

For example, consider the following sequence of events, assuming that version 1 of the relevant asset pack is already available locally:

1. Your app calls [`assetPack(withID:)`](assetpackmanifest/assetpack(withid:).md) on the [`AssetPackManifest`](assetpackmanifest.md) instance that [`manifest`](assetpackmanager/manifest.md) returns to obtain an [`AssetPack`](assetpack.md) instance.
2. The asset pack is updated to version 2 on the server.
3. Your app calls this method, passing the [`AssetPack`](assetpack.md) instance from step 1.

In this case, the returned status value will indicate that the downloaded asset pack is up to date. Generally, you shouldn’t need to handle this type of situation explicitly because the system automatically polls for updates periodically in the background.

This method doesn’t automatically trigger any downloads, updates, or removals.

## Parameters

- `assetPack`: The asset pack.

## See Also

- [func checkForUpdates() async throws -> (updatingIDs: Set<String>, removedIDs: Set<String>)](assetpackmanager/checkforupdates.md)
  Gets the latest asset-pack information from the server, updates outdated asset packs, and removes obsolete asset packs.
- [func ensureLocalAvailability(of: AssetPack, requireLatestVersion: Bool) async throws](assetpackmanager/ensurelocalavailability(of:requirelatestversion:).md)
  Ensures that an asset pack is available locally, performing a download if necessary.
- [func ensureLocalAvailability(of: Set<AssetPack>, requireLatestVersions: Bool) async throws](assetpackmanager/ensurelocalavailability(of:requirelatestversions:).md)
  Ensures the specified asset packs are available locally, performing a batch download if necessary.
- [func assetPackIsAvailableLocally(withID: String) -> Bool](assetpackmanager/assetpackisavailablelocally(withid:).md)
  Checks whether an asset pack is available locally.
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

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/status(relativeto:))*