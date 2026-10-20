# AssetPack.Status

**Framework**: Background Assets  
**Kind**: struct  
**Role**: Structure

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
- [static let downloadAvailable: AssetPack.Status](./status/downloadavailable.md)
  A status value that indicates that the asset pack is available to download.
- [static let downloading: AssetPack.Status](./status/downloading.md)
  A status value that indicates that the system is currently downloading the asset pack.
- [static let downloaded: AssetPack.Status](./status/downloaded.md)
  A status value that indicates that the system finished downloading the asset pack.
### Updating assets
- [static let upToDate: AssetPack.Status](./status/uptodate.md)
  A status value that indicates that the downloaded asset pack is up to date.
- [static let outOfDate: AssetPack.Status](./status/outofdate.md)
  A status value that indicates that the downloaded asset pack is out of date.
- [static let obsolete: AssetPack.Status](./status/obsolete.md)
  A status value that indicates that the asset pack is no longer available to download.
- [static let updateAvailable: AssetPack.Status](./status/updateavailable.md)
  A status value that indicates that an update to the asset pack is available to download.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Accessing asset details
- [let userInfo: Data?](./userinfo.md)
  JSON-encoded custom information that’s associated with the asset pack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpack/status)*