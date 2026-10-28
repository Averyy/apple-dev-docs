# checkForUpdates()

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Gets the latest asset-pack information from the server, updates outdated asset packs, and removes obsolete asset packs.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@discardableResult
func checkForUpdates() async throws -> (updatingIDs: Set<String>, removedIDs: Set<String>)
```

## Return Value

A 2-tuple with the set of IDs of asset packs that are being updated and the set of IDs of asset packs that were removed as a result of the check for updates. Neither updates nor removals that weren’t triggered by the check for updates are taken into account.

## Discussion

This method waits for any downloads that it schedules to be registered with the download manager, but it doesn’t wait for those downloads to begin or to finish. If you want to monitor download progress, then you should await status updates on [`statusUpdates`](./statusupdates.md) or [`statusUpdates(forAssetPackWithID:)`](./statusupdates%28forassetpackwithid%29.md).

## See Also

### Managing asset packs
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
- [func ensureLocalAvailability(of: AssetPack) async throws](./ensurelocalavailability%28of%29.md)
  Ensures that the specified asset pack is available locally, performing a download if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/checkforupdates())*