# authorizationStatus

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The current authorization status for the app.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var authorizationStatus: CLAuthorizationStatus { get }
```

```objc
@property (nonatomic, readonly) CLAuthorizationStatus authorizationStatus;
```

## Mentions

- [Requesting authorization to use location services](../requesting-authorization-to-use-location-services.md)

#### Return Value

A value indicating whether the app is authorized to use location services.

#### Discussion

Check this value when the [`locationManagerDidChangeAuthorization(_:)`](../cllocationmanagerdelegate/locationmanagerdidchangeauthorization%28_%29.md) delegate callback indicates that the authorization status has changed.

The system is guaranteed to call the delegate method with the app’s initial authorization state and all authorization status changes.

The system manages the authorization status of a given app according to several factors. Users must authorize the app to use location services explicitly, and location services must be enabled in Settings > Privacy. See [Choosing the  Location Services Authorization to Request](../../BundleResources/choosing-the-location-services-authorization-to-request.md) for more information.

## See Also

### Requesting authorization for location services
- [func requestWhenInUseAuthorization()](./requestwheninuseauthorization%28%29.md)
  Requests the user’s permission to use location services while the app is in use.
- [func requestAlwaysAuthorization()](./requestalwaysauthorization%28%29.md)
  Requests the user’s permission to use location services regardless of whether the app is in use.
- [func requestTemporaryFullAccuracyAuthorization(withPurposeKey: String, completion: (((any Error)?) -> Void)?)](./requesttemporaryfullaccuracyauthorization%28withpurposekey,completion%29.md)
  Requests permission to temporarily use location services with full accuracy and reports the results to the provided completion handler.
- [func requestTemporaryFullAccuracyAuthorization(withPurposeKey: String)](./requesttemporaryfullaccuracyauthorization%28withpurposekey%29.md)
  Requests permission to temporarily use location services with full accuracy.
- [enum CLAuthorizationStatus](../clauthorizationstatus.md)
  Constants that indicate the app’s authorization to use location services.
- [NSLocationDefaultAccuracyReduced](../../BundleResources/information-property-list/nslocationdefaultaccuracyreduced.md)
  A Boolean value that indicates whether the app requests reduced location accuracy by default.
- [NSLocationAlwaysAndWhenInUseUsageDescription](../../BundleResources/information-property-list/nslocationalwaysandwheninuseusagedescription.md)
  A message that tells people why the app is requesting access to their location information at all times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/authorizationstatus-swift.property)*