# statusUpdates

**Framework**: Background Assets  
**Kind**: property

An asynchronous sequence of download-status updates for all asset packs.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
var statusUpdates: some Sendable & AsyncSequence<AssetPackManager.DownloadStatusUpdate, Never> { get }
```

#### Discussion

The sequence never finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/statusupdates)*