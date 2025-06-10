# checkForUpdates()

**Framework**: Background Assets  
**Kind**: method

Gets the latest asset-pack information from the server, updates outdated asset packs, and removes obsolete asset packs.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@discardableResult
func checkForUpdates() async throws -> (updatingIDs: Set<String>, removedIDs: Set<String>)
```

#### Return Value

A 2-tuple with the set of IDs of asset packs that are being updated and the set of IDs of asset packs that were removed as a result of the check for updates. Neither updates nor removals that weren’t triggered by the check for updates are taken into account.

#### Discussion

This method waits for any downloads that it schedules to be registered with the internal download system, but it doesn’t wait for those downloads to begin or to finish. If you want to monitor download progress, then you should await status updates on [`statusUpdates`](assetpackmanager/statusupdates.md) or [`statusUpdates(forAssetPackWithID:)`](assetpackmanager/statusupdates(forassetpackwithid:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/checkforupdates())*