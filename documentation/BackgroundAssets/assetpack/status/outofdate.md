# outOfDate

**Framework**: Background Assets  
**Kind**: property

A status value that indicates that the downloaded asset pack is out of date.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static let outOfDate: AssetPack.Status
```

#### Discussion

The presence of this status value doesn’t necessarily imply that an update to the asset pack can be downloaded over the current network connection. Check for the presence of [`downloadAvailable`](assetpack/status/downloadavailable.md) to determine whether an update can currently be downloaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpack/status/outofdate)*