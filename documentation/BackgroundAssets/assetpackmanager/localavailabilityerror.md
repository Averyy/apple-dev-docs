# AssetPackManager.LocalAvailabilityError

**Framework**: Background Assets  
**Kind**: struct

An error that provides information about local asset pack availability, distinguishing between successes and failures.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct LocalAvailabilityError
```

## Mentions

- [Reducing download and storage demands with localized asset packs](reducing-download-and-storage-demands-with-localized-asset-packs.md)

#### Overview

Inspect the [`successes`](assetpackmanager/localavailabilityerror/successes.md) property to determine the asset packs for which the system successfully ensured availability. The [`failures`](assetpackmanager/localavailabilityerror/failures.md) property provides a dictionary that maps from asset packs to errors that detail why the system couldn’t ensure their local availability.

## Topics

### Accessing availability status
- [let successes: Set<AssetPack>](assetpackmanager/localavailabilityerror/successes.md)
  A set of asset packs for which the system successfully ensured local availability.
- [let failures: [AssetPack : any Error]](assetpackmanager/localavailabilityerror/failures.md)
  A dictionary that maps asset packs to errors describing why the system couldn’t ensure their local availability.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum ManagedBackgroundAssetsError](managedbackgroundassetserror.md)
  An error for a managed asset pack.
- [let BAErrorDomain: String](baerrordomain.md)
- [enum BAErrorCode](baerrorcode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/localavailabilityerror)*