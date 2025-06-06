# CLAccuracyAuthorization

**Framework**: Core Location  
**Kind**: enum

Constants that indicate the level of location accuracy the app has authorization to use.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum CLAccuracyAuthorization
```

## Topics

### Getting the location accuracy
- [CLAccuracyAuthorization.fullAccuracy](claccuracyauthorization/fullaccuracy.md)
  The user authorized the app to access location data with full accuracy.
- [CLAccuracyAuthorization.reducedAccuracy](claccuracyauthorization/reducedaccuracy.md)
  The user authorized the app to access location data with reduced accuracy.
### Initializers
- [init?(rawValue: Int)](claccuracyauthorization/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Requesting authorization to use location services](requesting-authorization-to-use-location-services.md)
  Obtain authorization to use location services and manage changes to your app’s authorization status.
- [Suspending authorization requests](suspending-authorization-requests.md)
  Defer the system’s authorization request dialog until your app is ready.
- [enum CLAuthorizationStatus](clauthorizationstatus.md)
  Constants that indicate the app’s authorization to use location services.
- [NSLocationAlwaysAndWhenInUseUsageDescription](../BundleResources/Information-Property-List/NSLocationAlwaysAndWhenInUseUsageDescription.md)
  A message that tells the user why the app is requesting access to the user’s location information at all times.
- [NSLocationWhenInUseUsageDescription](../BundleResources/Information-Property-List/NSLocationWhenInUseUsageDescription.md)
  A message that tells the user why the app is requesting access to the user’s location information while the app is running in the foreground.
- [NSLocationUsageDescription](../BundleResources/Information-Property-List/NSLocationUsageDescription.md)
  A message that tells the user why the app is requesting access to the user’s location information.
- [NSLocationDefaultAccuracyReduced](../BundleResources/Information-Property-List/NSLocationDefaultAccuracyReduced.md)
  A Boolean value that indicates whether the app requests reduced location accuracy by default.
- [NSLocationAlwaysUsageDescription](../BundleResources/Information-Property-List/NSLocationAlwaysUsageDescription.md)
  A message that tells the user why the app is requesting access to the user’s location at all times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/claccuracyauthorization)*