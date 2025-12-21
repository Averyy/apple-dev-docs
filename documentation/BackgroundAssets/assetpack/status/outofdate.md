# outOfDate

**Framework**: Background Assets  
**Kind**: property

A status value that indicates that the downloaded asset pack is out of date.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static let outOfDate: AssetPack.Status
```

#### Discussion

The presence of this status value doesn’t necessarily imply that an update to the asset pack can be downloaded over the current network connection. Check for the presence of [`downloadAvailable`](assetpack/status/downloadavailable.md) to determine whether an update can currently be downloaded.

## See Also

- [static let upToDate: AssetPack.Status](assetpack/status/uptodate.md)
  A status value that indicates that the downloaded asset pack is up to date.
- [static let obsolete: AssetPack.Status](assetpack/status/obsolete.md)
  A status value that indicates that the asset pack is no longer available to download.
- [static let updateAvailable: AssetPack.Status](assetpack/status/updateavailable.md)
  A status value that indicates that an update to the asset pack is available to download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpack/status/outofdate)*