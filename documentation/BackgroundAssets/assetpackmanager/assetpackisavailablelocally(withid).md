# assetPackIsAvailableLocally(withID:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Checks whether an asset pack is available locally.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+

## Declaration

```swift
nonisolated
func assetPackIsAvailableLocally(withID assetPackID: String) -> Bool
```

#### Return Value

Whether the asset pack is available locally.

## Parameters

- `assetPackID`: The asset pack’s ID.

## See Also

### Managing asset packs
- [func checkForUpdates() async throws -> (updatingIDs: Set<String>, removedIDs: Set<String>)](./checkforupdates%28%29.md)
  Gets the latest asset-pack information from the server, updates outdated asset packs, and removes obsolete asset packs.
- [func ensureLocalAvailability(of: AssetPack, requireLatestVersion: Bool) async throws](./ensurelocalavailability%28of,requirelatestversion%29.md)
  Ensures that an asset pack is available locally, performing a download if necessary.
- [func ensureLocalAvailability(of: Set<AssetPack>, requireLatestVersions: Bool) async throws](./ensurelocalavailability%28of,requirelatestversions%29.md)
  Ensures the specified asset packs are available locally, performing a batch download if necessary.
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

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/assetpackisavailablelocally(withid:))*