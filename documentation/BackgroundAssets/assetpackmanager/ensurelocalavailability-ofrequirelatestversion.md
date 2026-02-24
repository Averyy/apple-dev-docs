# ensureLocalAvailability(of:requireLatestVersion:)

**Framework**: Background Assets  
**Kind**: method

Ensures that the specified asset pack be available locally.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- tvOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)

## Declaration

```swift
func ensureLocalAvailability(of assetPack: AssetPack, requireLatestVersion shouldUpdate: Bool = false) async throws
```

#### Discussion

This method checks if the asset pack is currently downloaded. If it isn’t, then it schedules it to be downloaded and waits for the download to complete. It’s guaranteed that the requested asset pack will be available locally once this method returns without throwing. If the method throws, then the asset pack is **not** guaranteed to be available locally. You can optionally monitor download progress by awaiting status updates from [`statusUpdates`](assetpackmanager/statusupdates.md) or [`statusUpdates(forAssetPackWithID:)`](assetpackmanager/statusupdates(forassetpackwithid:).md) in a different task.

> **Note**: When the asset pack can’t be downloaded.

## Parameters

- `assetPack`: The asset pack the local availability of which to ensure.
- `shouldUpdate`: Whether to require that the latest version be available locally. When `true` is passed to this parameter, the method will wait for the update (if there indeed is one available) to be downloaded before returning. When `false` is passed, the method won’t check for updates and won’t attempt to download any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/ensurelocalavailability(of:requirelatestversion:))*