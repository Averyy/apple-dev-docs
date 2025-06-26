# assetPack(withID:)

**Framework**: Background Assets  
**Kind**: method

Gets a representation of an asset pack.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func assetPack(withID assetPackID: String) async throws -> AssetPack
```

## Mentions

- [Downloading asset packs hosted by Apple](downloading-asset-packs-hosted-by-apple.md)

#### Return Value

A representation of the asset pack.

#### Discussion

This method might attempt to get the latest asset-pack information from the server.

- Throws [`ManagedBackgroundAssetsError.assetPackNotFound(withID:)`](managedbackgroundassetserror/assetpacknotfound(withid:).md) when no asset pack with the specified ID is found.

## Parameters

- `assetPackID`: The asset pack’s ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/assetpack(withid:))*