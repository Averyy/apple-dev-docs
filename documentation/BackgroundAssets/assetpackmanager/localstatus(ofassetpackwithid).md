# localStatus(ofAssetPackWithID:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Checks an asset pack’s local status.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+

## Declaration

```swift
func localStatus(ofAssetPackWithID assetPackID: String) async -> AssetPack.Status
```

#### Return Value

The asset pack’s local status.

#### Discussion

This method checks only status values that are determinable offline. It doesn’t induce any network traffic or automatically trigger any downloads, updates, or removals. The following status values are determinable offline:

- [`outOfDate`](../assetpack/status/outofdate.md) (in some situations)
- [`obsolete`](../assetpack/status/obsolete.md) (in some situations)
- [`downloaded`](../assetpack/status/downloaded.md)

Because this method doesn’t communicate with the server, it can’t determine whether a particular asset pack exists in the first place. Instead, it returns an empty status value when provided a nonexistent asset-pack ID, which is indistinguishable from the situation in which the asset pack does indeed exist but hasn’t yet been downloaded. Use [`status(ofAssetPackWithID:)`](./status%28ofassetpackwithid%29.md) to get a full view of an asset pack’s status.

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
- [func assetPackIsAvailableLocally(withID: String) -> Bool](./assetpackisavailablelocally%28withid%29.md)
  Checks whether an asset pack is available locally.
- [func status(relativeTo: AssetPack) async throws -> AssetPack.Status](./status%28relativeto%29.md)
  Checks the current status relative to a particular asset pack.
- [AssetPack.Status](../assetpack/status.md)
  The status of an asset pack.
- [func remove(assetPackWithID: String) async throws](./remove%28assetpackwithid%29.md)
  Removes the specified asset pack from the device.
- [func status(ofAssetPackWithID: String) async throws -> AssetPack.Status](./status%28ofassetpackwithid%29.md)
  Checks an asset pack’s status.
- [func ensureLocalAvailability(of: AssetPack) async throws](./ensurelocalavailability%28of%29.md)
  Ensures that the specified asset pack is available locally, performing a download if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/localstatus(ofassetpackwithid:))*