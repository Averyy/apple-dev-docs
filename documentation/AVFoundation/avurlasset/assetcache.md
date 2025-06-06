# assetCache

**Framework**: AVFoundation  
**Kind**: property

The asset’s associated asset cache, if it exists.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var assetCache: AVAssetCache? { get }
```

#### Discussion

This property provides access to an instance of [`AVAssetCache`](avassetcache.md) to use for inspection of locally cached media data. The value of this property is `nil` if you haven’t configured the asset to store or access media data from disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasset/assetcache)*