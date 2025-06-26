# allAssetPacks

**Framework**: Background Assets  
**Kind**: property

The asset packs that are available to download.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var allAssetPacks: Set<AssetPack> { get async throws }
```

#### Discussion

Accessing this property might cause an attempt to get the latest asset-pack information from the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/allassetpacks)*