# locationManager(_:didUpdateTo:from:)

**Framework**: Core Location  
**Kind**: method

Tells the delegate that a new location value is available.

**Availability**:
- macOS 10.6+

## Declaration

```swift
optional func locationManager(_ manager: CLLocationManager, didUpdateTo newLocation: CLLocation, from oldLocation: CLLocation)
```

#### Discussion

By the time this message is delivered to your delegate, the new location data is also available directly from the [`CLLocationManager`](cllocationmanager.md) object. The `newLocation` parameter may contain the data that was cached from a previous usage of the location service. You can use the `CLLocation/timestamp` property of the location object to determine how recent the location data is.

## Parameters

- `manager`: The location manager object that generated the update event.
- `newLocation`: The new location data.
- `oldLocation`: The location data from the previous update. If this is the first update event delivered by this location manager, this parameter is  .

## See Also

- [func locationManager(CLLocationManager, didUpdateLocations: [CLLocation])](cllocationmanagerdelegate/locationmanager(_:didupdatelocations:).md)
  Tells the delegate that new location data is available.
- [func locationManager(CLLocationManager, didFinishDeferredUpdatesWithError: (any Error)?)](cllocationmanagerdelegate/locationmanager(_:didfinishdeferredupdateswitherror:).md)
  Tells the delegate that updates will no longer be deferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didupdateto:from:))*