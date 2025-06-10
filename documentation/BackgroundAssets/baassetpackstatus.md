# BAAssetPackStatus

**Framework**: Background Assets  
**Kind**: struct

The status of an asset pack.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct BAAssetPackStatus
```

## Topics

### Initializers
- [init(rawValue: UInt)](baassetpackstatus/init(rawvalue:).md)
### Type Properties
- [static var downloadAvailable: BAAssetPackStatus](baassetpackstatus/downloadavailable.md)
  A status value that indicates that the asset pack is available to download.
- [static var downloaded: BAAssetPackStatus](baassetpackstatus/downloaded.md)
  A status value that indicates that the system finished downloading the asset pack.
- [static var downloading: BAAssetPackStatus](baassetpackstatus/downloading.md)
  A status value that indicates that the system is currently downloading the asset pack.
- [static var obsolete: BAAssetPackStatus](baassetpackstatus/obsolete.md)
  A status value that indicates that the asset pack is no longer available to download.
- [static var outOfDate: BAAssetPackStatus](baassetpackstatus/outofdate.md)
  A status value that indicates that the downloaded asset pack is out of date.
- [static var upToDate: BAAssetPackStatus](baassetpackstatus/uptodate.md)
  A status value that indicates that the downloaded asset pack is up to date.
- [static var updateAvailable: BAAssetPackStatus](baassetpackstatus/updateavailable.md)
  A status value that indicates that an update to the asset pack is available to download.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackstatus)*