# AssetPack.Status

**Framework**: Background Assets  
**Kind**: struct

The status of an asset pack.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Status
```

## Topics

### Tracking downloads
- [static let downloadAvailable: AssetPack.Status](assetpack/status/downloadavailable.md)
  A status value that indicates that the asset pack is available to download.
- [static let downloading: AssetPack.Status](assetpack/status/downloading.md)
  A status value that indicates that the system is currently downloading the asset pack.
- [static let downloaded: AssetPack.Status](assetpack/status/downloaded.md)
  A status value that indicates that the system finished downloading the asset pack.
### Updating assets
- [static let upToDate: AssetPack.Status](assetpack/status/uptodate.md)
  A status value that indicates that the downloaded asset pack is up to date.
- [static let outOfDate: AssetPack.Status](assetpack/status/outofdate.md)
  A status value that indicates that the downloaded asset pack is out of date.
- [static let obsolete: AssetPack.Status](assetpack/status/obsolete.md)
  A status value that indicates that the asset pack is no longer available to download.
- [static let updateAvailable: AssetPack.Status](assetpack/status/updateavailable.md)
  A status value that indicates that an update to the asset pack is available to download.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [let userInfo: Data?](assetpack/userinfo.md)
  JSON-encoded custom information that’s associated with the asset pack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpack/status)*