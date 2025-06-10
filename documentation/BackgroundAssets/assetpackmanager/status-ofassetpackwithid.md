# status(ofAssetPackWithID:)

**Framework**: Background Assets  
**Kind**: method

Gets the status of the asset pack with the specified ID.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func status(ofAssetPackWithID assetPackID: String) async throws -> AssetPack.Status
```

#### Return Value

The asset pack’s status.

#### Discussion

This method attempts to get the latest asset-pack information from the server. No updates or removals are automatically triggered.

> **Note**: [`ManagedBackgroundAssetsError.assetPackNotFound(withID:)`](managedbackgroundassetserror/assetpacknotfound(withid:).md) when no asset pack with the specified ID is found.

## Parameters

- `assetPackID`: The ID of the asset pack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/status(ofassetpackwithid:))*