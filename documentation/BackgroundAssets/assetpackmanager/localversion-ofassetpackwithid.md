# localVersion(ofAssetPackWithID:)

**Framework**: Background Assets  
**Kind**: method

Returns a locally available asset pack’s version number.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- macOS 27.2+ (Beta)
- tvOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)

## Declaration

```swift
nonisolated
func localVersion(ofAssetPackWithID assetPackID: String) throws -> Int
```

#### Return Value

The asset pack’s version number.

#### Discussion

> **Note**: [`ManagedBackgroundAssetsError.assetPackNotFound(withID:)`](managedbackgroundassetserror/assetpacknotfound(withid:).md) when no asset pack with the specified ID is available locally.

## Parameters

- `assetPackID`: The asset pack’s ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/localversion(ofassetpackwithid:))*