# cinematicCapability(for:)

**Framework**: Cinematic  
**Kind**: method

Asynchronously checks the cinematic capability of an asset. Returns CNCinematicCapability.none if a cinematic metadata track is not present. CNCinematicCapability.renderable if the cinematic asset can be used without preprocessing CNCinematicCapability.needsPreprocessing If cinematic asset needs preprocessing before it can be used For assets that need preprocessing use `CNAssetInfo.preprocessAsset(configuration:subprogress:)` before using the asset

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst ?+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
class func cinematicCapability(for asset: AVAsset) async -> CNCinematicCapability
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnassetinfo-2ata2/cinematiccapability(for:))*