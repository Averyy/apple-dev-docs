# checkForUpdates()

**Framework**: Background Assets  
**Kind**: method

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

#### Return Value

A 2-tuple with the set of IDs of asset packs that are being updated and the set of IDs of asset packs that were removed as a result of the check for updates. Neither updates nor removals that weren’t triggered by the check for updates are taken into account.

#### Discussion

This method waits for any downloads that it schedules to be registered with the download manager, but it doesn’t wait for those downloads to begin or to finish. If you want to monitor download progress, then you should await status updates on [`statusUpdates`](assetpackmanager/statusupdates.md) or [`statusUpdates(forAssetPackWithID:)`](assetpackmanager/statusupdates(forassetpackwithid:).md).

## See Also

- [func ensureLocalAvailability(of: AssetPack) async throws](assetpackmanager/ensurelocalavailability(of:).md)
  Ensures that the specified asset pack be available locally.
- [func remove(assetPackWithID: String) async throws](assetpackmanager/remove(assetpackwithid:).md)
  Removes the specified asset pack from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/checkforupdates())*