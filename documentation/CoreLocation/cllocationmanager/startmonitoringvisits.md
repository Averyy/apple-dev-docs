# startMonitoringVisits()

**Framework**: Core Location  
**Kind**: method

Starts the delivery of visit-related events.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
func startMonitoringVisits()
```

## Mentions

- [Getting the current location of a device](getting-the-current-location-of-a-device.md)

#### Discussion

Calling this method begins the delivery of visit-related events to your app. Enabling visit events for one location manager enables visit events for all other location manager objects in your app. When a new visit event arrives, the location manager object delivers the event to the [`locationManager(_:didVisit:)`](cllocationmanagerdelegate/locationmanager(_:didvisit:).md) method of its delegate.

Your app can monitor for visit events without calling `requestTemporaryPreciseLocationAuthorization(withPurposeKey:)`. In that case, the visit events use reduced accuracy, as reflected by the [`horizontalAccuracy`](clvisit/horizontalaccuracy.md) property of [`CLVisit`](clvisit.md).

If your app is terminated while this service is active, the system relaunches your app when new visit events are ready to be delivered. Upon relaunch, recreate your location manager object and assign a delegate to begin receiving visit events. You don’t need to call this method again to restart the delivery of visit events, but calling it does no harm.

If a compatible iPad or iPhone app calls this method when running in visionOS, the method does nothing.

## See Also

- [func stopMonitoringVisits()](cllocationmanager/stopmonitoringvisits.md)
  Stops the delivery of visit-related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/startmonitoringvisits())*