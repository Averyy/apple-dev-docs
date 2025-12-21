# requestAlwaysAuthorization()

**Framework**: Core Location  
**Kind**: method

Requests the user’s permission to use location services regardless of whether the app is in use.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
func requestAlwaysAuthorization()
```

## Mentions

- [Creating a location push service extension](creating-a-location-push-service-extension.md)

#### Discussion

You must call this or the [`requestWhenInUseAuthorization()`](cllocationmanager/requestwheninuseauthorization().md) method before your app can receive location information. To call this method, you must have both [`NSLocationAlwaysUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocationAlwaysUsageDescription) and [`NSLocationWhenInUseUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocationWhenInUseUsageDescription) keys in your app’s `Info.plist` file. You may call [`requestAlwaysAuthorization()`](cllocationmanager/requestalwaysauthorization().md) when the current authorization state is either:

- Not Determined — [`CLAuthorizationStatus.notDetermined`](clauthorizationstatus/notdetermined.md)
- When In Use — [`CLAuthorizationStatus.authorizedWhenInUse`](clauthorizationstatus/authorizedwheninuse.md)

Use the [`locationManager(_:didUpdateLocations:)`](cllocationmanagerdelegate/locationmanager(_:didupdatelocations:).md) method on the [`CLLocationManager`](cllocationmanager.md) delegate to receive updates when the user makes permission choices.

Core Location limits calls to [`requestAlwaysAuthorization()`](cllocationmanager/requestalwaysauthorization().md). After your app calls this method, further calls have no effect. If a compatible iPad or iPhone app calls this method when running in visionOS, the method treats it as a request for When in Use authorization instead.

##### Request Always Authorization After Getting When in Use

To obtain Always authorization, your app must first request When In Use permission followed by requesting Always authorization.

If the user grants When In Use permission after your app calls [`requestWhenInUseAuthorization()`](cllocationmanager/requestwheninuseauthorization().md), then calling [`requestAlwaysAuthorization()`](cllocationmanager/requestalwaysauthorization().md) immediately prompts the user to request Always permission. If the user responded to [`requestWhenInUseAuthorization()`](cllocationmanager/requestwheninuseauthorization().md) with Allow Once, then Core Location ignores further calls to [`requestAlwaysAuthorization()`](cllocationmanager/requestalwaysauthorization().md) due to the temporary authorization.

> **Note**:  In iOS 16 and later, apps that actively track a user’s location or that have recently enabled Core Location display an indicator in Control Center. Be mindful of battery use and user privacy by monitoring the device’s location only when necessary and when the user expects it.

Core Location prompts the user to grant permission with the string from [`NSLocationAlwaysUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocationAlwaysUsageDescription). The user prompt displays the following options, which determine the authorization your app can receive:

| Option | Authorization |
| --- | --- |
| Keep Only While Using | Core Location leaves the authorization as When In Use. The delegate doesn’t receive any updates. |
| Change to Always Allow | Core Location grants your app Always authorization. The delegate receives [`CLAuthorizationStatus.authorizedAlways`](clauthorizationstatus/authorizedalways.md). |

##### Request Always Authorization Directly

If your app’s current state is [`CLAuthorizationStatus.notDetermined`](clauthorizationstatus/notdetermined.md) and you call [`requestAlwaysAuthorization()`](cllocationmanager/requestalwaysauthorization().md), Core Location uses two prompts before it fully enables Always authorization.

The first prompt displays immediately with the string from [`NSLocationWhenInUseUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocationWhenInUseUsageDescription). The user prompt displays the following options, which determine the authorization your app receives:

| Option | Authorization |
| --- | --- |
| Allow While Using App | Core Location grants your app a Provisional Always authorization. The delegate receives [`CLAuthorizationStatus.authorizedAlways`](clauthorizationstatus/authorizedalways.md). |
| Allow Once | Core Location grants your app a Temporary When in Use authorization. The delegate receives [`CLAuthorizationStatus.authorizedWhenInUse`](clauthorizationstatus/authorizedwheninuse.md). This authorization expires when your app is no longer in use, reverting to [`CLAuthorizationStatus.notDetermined`](clauthorizationstatus/notdetermined.md). |
| Don’t Allow | Core Location marks your app with Denied authorization. The delegate receives [`CLAuthorizationStatus.denied`](clauthorizationstatus/denied.md). |

The second prompt displays when Core Location prepares to deliver an event to your app requiring [`CLAuthorizationStatus.authorizedAlways`](clauthorizationstatus/authorizedalways.md). If the app is in the Provisional Always state, the system displays the second prompt with the string from [`NSLocationAlwaysUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocationAlwaysUsageDescription). Core Location will typically display the second prompt when your app isn’t running.

Your app receives permanent Always authorization if the user chooses to grant permission when the second prompt appears while in the Provisional Always state. When the user responds, your app receives either the location event or a call to your delegate with the modified authorization.

When displaying the second prompt, the user sees one of the following options:

| Option | Authorization |
| --- | --- |
| Keep Only While Using | Core Location changes the authorization to When In Use. The delegate receives [`CLAuthorizationStatus.authorizedWhenInUse`](clauthorizationstatus/authorizedwheninuse.md). |
| Change to Always Allow | Core Location removes the provisional status, making the Always authorization permanent. The delegate doesn’t receive a callback. |

If the user responds to the prompt near the time it was delivered and chooses to allow the Always permission, the location event will be delivered to your app.

## Topics

### Related Documentation
- [NSLocationAlwaysUsageDescription](../BundleResources/Information-Property-List/NSLocationAlwaysUsageDescription.md)
  A message that tells people why the app is requesting access to their location at all times.

## See Also

- [func requestWhenInUseAuthorization()](cllocationmanager/requestwheninuseauthorization.md)
  Requests the user’s permission to use location services while the app is in use.
- [func requestTemporaryFullAccuracyAuthorization(withPurposeKey: String, completion: (((any Error)?) -> Void)?)](cllocationmanager/requesttemporaryfullaccuracyauthorization(withpurposekey:completion:).md)
  Requests permission to temporarily use location services with full accuracy and reports the results to the provided completion handler.
- [func requestTemporaryFullAccuracyAuthorization(withPurposeKey: String)](cllocationmanager/requesttemporaryfullaccuracyauthorization(withpurposekey:).md)
  Requests permission to temporarily use location services with full accuracy.
- [var authorizationStatus: CLAuthorizationStatus](cllocationmanager/authorizationstatus-swift.property.md)
  The current authorization status for the app.
- [enum CLAuthorizationStatus](clauthorizationstatus.md)
  Constants that indicate the app’s authorization to use location services.
- [NSLocationDefaultAccuracyReduced](../BundleResources/Information-Property-List/NSLocationDefaultAccuracyReduced.md)
  A Boolean value that indicates whether the app requests reduced location accuracy by default.
- [NSLocationAlwaysAndWhenInUseUsageDescription](../BundleResources/Information-Property-List/NSLocationAlwaysAndWhenInUseUsageDescription.md)
  A message that tells people why the app is requesting access to their location information at all times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/requestalwaysauthorization())*