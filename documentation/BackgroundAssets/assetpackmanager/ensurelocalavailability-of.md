# ensureLocalAvailability(of:)

**Framework**: Background Assets  
**Kind**: method

Ensures that the specified asset pack be available locally.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func ensureLocalAvailability(of assetPack: AssetPack) async throws
```

#### Discussion

This method checks if the asset pack is currently downloaded. If it isn’t, then it schedules it to be downloaded and waits for the download to complete. It’s guaranteed that the requested asset pack will be available locally once this method returns without throwing. If the method throws, then the asset pack is  guaranteed to be available locally. You can optionally monitor download progress by awaiting status updates from [`statusUpdates`](assetpackmanager/statusupdates.md) or [`statusUpdates(forAssetPackWithID:)`](assetpackmanager/statusupdates(forassetpackwithid:).md) in a different task.

> **Note**: When the asset pack can’t be downloaded.

## Parameters

- `assetPack`: The asset pack the local availability of which to ensure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/ensurelocalavailability(of:))*