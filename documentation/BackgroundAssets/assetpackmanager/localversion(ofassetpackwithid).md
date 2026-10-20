# localVersion(ofAssetPackWithID:)

**Framework**: Background Assets  
**Kind**: method

Returns a locally available asset pack’s version number.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- tvOS 27.2+
- visionOS 27.2+

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