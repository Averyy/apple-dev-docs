# CLAuthorizationStatus

**Framework**: Core Location  
**Kind**: enum

Constants that indicate the app’s authorization to use location services.

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
enum CLAuthorizationStatus
```

#### Overview

Handle changes to authorization status in your location manager’s delegate method, [`locationManager(_:didChangeAuthorization:)`](cllocationmanagerdelegate/locationmanager(_:didchangeauthorization:).md).

## Topics

### Getting the authorization status
- [CLAuthorizationStatus.notDetermined](clauthorizationstatus/notdetermined.md)
  The user has not chosen whether the app can use location services.
- [CLAuthorizationStatus.restricted](clauthorizationstatus/restricted.md)
  The app is not authorized to use location services.
- [CLAuthorizationStatus.denied](clauthorizationstatus/denied.md)
  The user denied the use of location services for the app or they are disabled globally in Settings.
- [static var authorized: CLAuthorizationStatus](clauthorizationstatus/authorized.md)
  The user authorized the app to use location services.
- [CLAuthorizationStatus.authorizedAlways](clauthorizationstatus/authorizedalways.md)
  The user authorized the app to start location services at any time.
- [CLAuthorizationStatus.authorizedWhenInUse](clauthorizationstatus/authorizedwheninuse.md)
  The user authorized the app to start location services while it is in use.
### Initializers
- [init?(rawValue: Int32)](clauthorizationstatus/init(rawvalue:).md)

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
- [enum CLAccuracyAuthorization](claccuracyauthorization.md)
  Constants that indicate the level of location accuracy the app has authorization to use.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clauthorizationstatus)*