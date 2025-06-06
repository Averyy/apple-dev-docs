# requestLocation()

**Framework**: Core Location  
**Kind**: method

Requests the one-time delivery of the user’s current location.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func requestLocation()
```

## Mentions

- [Getting the current location of a device](getting-the-current-location-of-a-device.md)

#### Discussion

This method returns immediately. Calling it causes the location manager to obtain a location fix (which may take several seconds) and call the delegate’s [`locationManager(_:didUpdateLocations:)`](cllocationmanagerdelegate/locationmanager(_:didupdatelocations:).md) method with the result. The location fix is obtained at the accuracy level indicated by the [`desiredAccuracy`](cllocationmanager/desiredaccuracy.md) property. Only one location fix is reported to the delegate, after which location services are stopped. If a location fix cannot be determined in a timely manner, the location manager calls the delegate’s [`locationManager(_:didFailWithError:)`](cllocationmanagerdelegate/locationmanager(_:didfailwitherror:).md) method instead and reports a [`CLError.Code.locationUnknown`](clerror-swift.struct/code/locationunknown.md) error.

Use this method when you want the user’s current location but do not need to leave location services running. This method starts location services long enough to return a result or report an error and then stops them again. Calling the [`startUpdatingLocation()`](cllocationmanager/startupdatinglocation().md) or  [`allowDeferredLocationUpdates(untilTraveled:timeout:)`](cllocationmanager/allowdeferredlocationupdates(untiltraveled:timeout:).md) method cancels any pending request made using this method. Calling this method while location services are already running does nothing. To cancel a pending request, call the [`stopUpdatingLocation()`](cllocationmanager/stopupdatinglocation().md) method.

If obtaining the desired accuracy would take too long, the location manager delivers a less accurate location value rather than reporting an error.

When using this method, the associated delegate must implement the [`locationManager(_:didUpdateLocations:)`](cllocationmanagerdelegate/locationmanager(_:didupdatelocations:).md) and [`locationManager(_:didFailWithError:)`](cllocationmanagerdelegate/locationmanager(_:didfailwitherror:).md) methods. Failure to do so is a programmer error.

## See Also

- [func startUpdatingLocation()](cllocationmanager/startupdatinglocation.md)
  Starts the generation of updates that report the user’s current location.
- [func stopUpdatingLocation()](cllocationmanager/stopupdatinglocation.md)
  Stops the generation of location updates.
- [var pausesLocationUpdatesAutomatically: Bool](cllocationmanager/pauseslocationupdatesautomatically.md)
  A Boolean value that indicates whether the location-manager object may pause location updates.
- [var allowsBackgroundLocationUpdates: Bool](cllocationmanager/allowsbackgroundlocationupdates.md)
  A Boolean value that indicates whether the app receives location updates when running in the background.
- [var showsBackgroundLocationIndicator: Bool](cllocationmanager/showsbackgroundlocationindicator.md)
  A Boolean value that indicates whether the status bar changes its appearance when an app uses location services in the background.
- [var activityType: CLActivityType](cllocationmanager/activitytype.md)
  The type of activity the app expects the user to typically perform while in the app’s location session.
- [enum CLActivityType](clactivitytype.md)
  Constants that indicate the type of activity associated with location updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/requestlocation())*