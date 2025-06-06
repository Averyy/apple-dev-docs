# locationManagerDidResumeLocationUpdates(_:)

**Framework**: Core Location  
**Kind**: method

Tells the delegate that the delivery of location updates has resumed.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
optional func locationManagerDidResumeLocationUpdates(_ manager: CLLocationManager)
```

#### Discussion

When you restart location services after an automatic pause, Core Location calls this method to notify your app that services have resumed. You are responsible for restarting location services in your app. Core Location does not resume updates automatically after it pauses them. For tips on how to restart location services when a pause occurs, see the discussion of the [`locationManagerDidPauseLocationUpdates(_:)`](cllocationmanagerdelegate/locationmanagerdidpauselocationupdates(_:).md) method.

## Parameters

- `manager`: The location manager that resumed the delivery of events.

## See Also

- [func locationManagerDidPauseLocationUpdates(CLLocationManager)](cllocationmanagerdelegate/locationmanagerdidpauselocationupdates(_:).md)
  Tells the delegate that location updates were paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanagerdidresumelocationupdates(_:))*