# locationManager(_:didFinishDeferredUpdatesWithError:)

**Framework**: Core Location  
**Kind**: method

Tells the delegate that updates will no longer be deferred.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
optional func locationManager(_ manager: CLLocationManager, didFinishDeferredUpdatesWithError error: (any Error)?)
```

#### Discussion

The location manager object calls this method to let you know that it has stopped deferring the delivery of location events. The manager may call this method for any number of reasons. For example, it calls it when you stop location updates altogether, when you ask the location manager to disallow deferred updates, or when a condition for deferring updates (such as exceeding a timeout or distance parameter) is met.

## Parameters

- `manager`: The location manager object that generated the update event.
- `error`: The error object containing the reason deferred location updates could not be delivered.

## See Also

- [func locationManager(CLLocationManager, didUpdateLocations: [CLLocation])](cllocationmanagerdelegate/locationmanager(_:didupdatelocations:).md)
  Tells the delegate that new location data is available.
- [func locationManager(CLLocationManager, didUpdateTo: CLLocation, from: CLLocation)](cllocationmanagerdelegate/locationmanager(_:didupdateto:from:).md)
  Tells the delegate that a new location value is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didfinishdeferredupdateswitherror:))*