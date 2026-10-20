# CLAccuracyAuthorization

**Framework**: Core Location  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum CLAccuracyAuthorization : NSInteger;
```

## Topics

### Getting the location accuracy
- [CLAccuracyAuthorization.fullAccuracy](./claccuracyauthorization/fullaccuracy.md)
  The user authorized the app to access location data with full accuracy.
- [CLAccuracyAuthorization.reducedAccuracy](./claccuracyauthorization/reducedaccuracy.md)
  The user authorized the app to access location data with reduced accuracy.
### Initializers
- [init?(rawValue: Int)](./claccuracyauthorization/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Authorization
- [Requesting authorization to use location services](./requesting-authorization-to-use-location-services.md)
  Obtain authorization to use location services and manage changes to your app’s authorization status.
- [Suspending authorization requests](./suspending-authorization-requests.md)
  Defer the system’s authorization request dialog until your app is ready.
- [enum CLAuthorizationStatus](./clauthorizationstatus.md)
  Constants that indicate the app’s authorization to use location services.
- [NSLocationAlwaysAndWhenInUseUsageDescription](../BundleResources/information-property-list/nslocationalwaysandwheninuseusagedescription.md)
  A message that tells people why the app is requesting access to their location information at all times.
- [NSLocationWhenInUseUsageDescription](../BundleResources/information-property-list/nslocationwheninuseusagedescription.md)
  A message that tells people why the app is requesting access to their location information while the app is running in the foreground.
- [NSLocationUsageDescription](../BundleResources/information-property-list/nslocationusagedescription.md)
  A message that tells people why the app is requesting access to their location information.
- [NSLocationDefaultAccuracyReduced](../BundleResources/information-property-list/nslocationdefaultaccuracyreduced.md)
  A Boolean value that indicates whether the app requests reduced location accuracy by default.
- [NSLocationAlwaysUsageDescription](../BundleResources/information-property-list/nslocationalwaysusagedescription.md)
  A message that tells people why the app is requesting access to their location at all times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/claccuracyauthorization)*