# requestWhenInUseAuthorization()

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Requests the user’s permission to use location services while the app is in use.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func requestWhenInUseAuthorization()
```

```objc
- (void) requestWhenInUseAuthorization;
```

#### Discussion

You must call this method or [`requestAlwaysAuthorization()`](./requestalwaysauthorization%28%29.md) before you can receive location-related information. You may call [`requestWhenInUseAuthorization()`](./requestwheninuseauthorization%28%29.md) whenever the current authorization status is not determined ([`CLAuthorizationStatus.notDetermined`](../clauthorizationstatus/notdetermined.md)).

> ❗ **Important**:  Your app must be in the foreground to show a location authorization prompt.

This method runs asynchronously and prompts the user to grant permission to the app to use location services. The user prompt contains the text from the [`NSLocationWhenInUseUsageDescription`](../../BundleResources/information-property-list/nslocationwheninuseusagedescription.md) key in your app `Info.plist` file, and the presence of that key is required when calling this method. The user prompt displays the following options, which determine the authorization your app can receive.

| Option | Authorization |
| --- | --- |
| Allow While Using App | When In Use authorization that does not expire. |
| Allow Once | Temporary When In Use authorization that expires when the app is no longer in use. |
| Don’t Allow | Denied; no further authorization requests are allowed. |

After the user makes a selection and determines the status, the location manager delivers the results to the delegate’s [`locationManager(_:didChangeAuthorization:)`](../cllocationmanagerdelegate/locationmanager%28_,didchangeauthorization%29.md) method. If the initial authorization status is anything other than [`CLAuthorizationStatus.notDetermined`](../clauthorizationstatus/notdetermined.md), this method does nothing and doesn’t call the [`locationManager(_:didChangeAuthorization:)`](../cllocationmanagerdelegate/locationmanager%28_,didchangeauthorization%29.md) method.

If the user’s choice grants When In Use authorization to your app, your app can start any location service and is eligible to receive the results while it’s in use. If the user’s choice grants temporary When In Use authorization, the authorization expires when the app is no longer in use, reverting to Not Determined status ([`CLAuthorizationStatus.notDetermined`](../clauthorizationstatus/notdetermined.md)). For information about when an app is considered to be in use, see [Choosing the  Location Services Authorization to Request](../../BundleResources/choosing-the-location-services-authorization-to-request.md).

When your app starts standard location services in the foreground, they continue to run in the background if your app has enabled background location updates in the Capabilities tab of your Xcode project. Attempts to start location updates while your app runs in the background will fail. The system displays a location services indicator in the status bar when your app moves to the background with active location services.

> **Note**:  In iOS 16 and later, apps that actively track a user’s location or that have recently enabled Core Location display an indicator in Control Center. Be mindful of battery use and user privacy by monitoring the device’s location only when necessary and when the user expects it.

## Topics

### Related documentation
- [Handling location updates in the background](../handling-location-updates-in-the-background.md)
  Configure your app to receive location updates when it isn’t running in the foreground.
- [NSLocationWhenInUseUsageDescription](../../BundleResources/information-property-list/nslocationwheninuseusagedescription.md)
  A message that tells people why the app is requesting access to their location information while the app is running in the foreground.

## See Also

### Requesting authorization for location services
- [func requestAlwaysAuthorization()](./requestalwaysauthorization%28%29.md)
  Requests the user’s permission to use location services regardless of whether the app is in use.
- [func requestTemporaryFullAccuracyAuthorization(withPurposeKey: String, completion: (((any Error)?) -> Void)?)](./requesttemporaryfullaccuracyauthorization%28withpurposekey,completion%29.md)
  Requests permission to temporarily use location services with full accuracy and reports the results to the provided completion handler.
- [func requestTemporaryFullAccuracyAuthorization(withPurposeKey: String)](./requesttemporaryfullaccuracyauthorization%28withpurposekey%29.md)
  Requests permission to temporarily use location services with full accuracy.
- [var authorizationStatus: CLAuthorizationStatus](./authorizationstatus-swift.property.md)
  The current authorization status for the app.
- [enum CLAuthorizationStatus](../clauthorizationstatus.md)
  Constants that indicate the app’s authorization to use location services.
- [NSLocationDefaultAccuracyReduced](../../BundleResources/information-property-list/nslocationdefaultaccuracyreduced.md)
  A Boolean value that indicates whether the app requests reduced location accuracy by default.
- [NSLocationAlwaysAndWhenInUseUsageDescription](../../BundleResources/information-property-list/nslocationalwaysandwheninuseusagedescription.md)
  A message that tells people why the app is requesting access to their location information at all times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/requestwheninuseauthorization())*