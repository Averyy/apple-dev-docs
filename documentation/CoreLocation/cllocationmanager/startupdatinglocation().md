# startUpdatingLocation()

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Starts the generation of updates that report the user’s current location.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func startUpdatingLocation()
```

```objc
- (void) startUpdatingLocation;
```

## Mentions

- [Getting the current location of a device](../getting-the-current-location-of-a-device.md)

## Discussion

This method returns immediately. Calling this method causes the location manager to obtain an initial location fix (which may take several seconds) and notify your delegate by calling its [`locationManager(_:didUpdateLocations:)`](../cllocationmanagerdelegate/locationmanager%28_,didupdatelocations%29.md) method. After that, the receiver generates update events primarily when the value in the [`distanceFilter`](./distancefilter.md) property is exceeded. Updates may be delivered in other situations though. For example, the receiver may send another notification if the hardware gathers a more accurate location reading.

Calling this method several times in succession does not automatically result in new events being generated. Calling [`stopUpdatingLocation()`](./stopupdatinglocation%28%29.md) in between, however, does cause a new initial event to be sent the next time you call this method.

If you start this service and your app is suspended, the system stops the delivery of events until your app starts running again (either in the foreground or background). If your app is terminated, the delivery of new location events stops altogether. Therefore, if your app needs to receive location events while in the background, it must include the `UIBackgroundModes` key (with the `location` value) in its `Info.plist` file.

In addition to your delegate object implementing the [`locationManager(_:didUpdateLocations:)`](../cllocationmanagerdelegate/locationmanager%28_,didupdatelocations%29.md) method, it should also implement the [`locationManager(_:didFailWithError:)`](../cllocationmanagerdelegate/locationmanager%28_,didfailwitherror%29.md) method to respond to potential errors.

## See Also

### Running the standard location service
- [func stopUpdatingLocation()](./stopupdatinglocation%28%29.md)
  Stops the generation of location updates.
- [func requestLocation()](./requestlocation%28%29.md)
  Requests the one-time delivery of the user’s current location.
- [var pausesLocationUpdatesAutomatically: Bool](./pauseslocationupdatesautomatically.md)
  A Boolean value that indicates whether the location-manager object may pause location updates.
- [var allowsBackgroundLocationUpdates: Bool](./allowsbackgroundlocationupdates.md)
  A Boolean value that indicates whether the app receives location updates when running in the background.
- [var showsBackgroundLocationIndicator: Bool](./showsbackgroundlocationindicator.md)
  A Boolean value that indicates whether the status bar changes its appearance when an app uses location services in the background.
- [var activityType: CLActivityType](./activitytype.md)
  The type of activity the app expects the user to typically perform while in the app’s location session.
- [enum CLActivityType](../clactivitytype.md)
  Constants that indicate the type of activity associated with location updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/startupdatinglocation())*