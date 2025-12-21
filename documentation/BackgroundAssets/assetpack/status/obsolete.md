# obsolete

**Framework**: Background Assets  
**Kind**: property

A status value that indicates that the asset pack is no longer available to download.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static let obsolete: AssetPack.Status
```

#### Discussion

Obsolete asset packs can’t be updated, and they also can’t be redownloaded once removed.

## See Also

- [static let upToDate: AssetPack.Status](assetpack/status/uptodate.md)
  A status value that indicates that the downloaded asset pack is up to date.
- [static let outOfDate: AssetPack.Status](assetpack/status/outofdate.md)
  A status value that indicates that the downloaded asset pack is out of date.
- [static let updateAvailable: AssetPack.Status](assetpack/status/updateavailable.md)
  A status value that indicates that an update to the asset pack is available to download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpack/status/obsolete)*