# locationManager(_:didUpdateHeading:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the location manager received updated heading information.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
optional func locationManager(_ manager: CLLocationManager, didUpdateHeading newHeading: CLHeading)
```

```objc
- (void) locationManager:(CLLocationManager *) manager didUpdateHeading:(CLHeading *) newHeading;
```

## Mentions

- [Getting heading and course information](../getting-heading-and-course-information.md)

#### Discussion

Implementation of this method is optional but expected if you start heading updates using the [`startUpdatingHeading()`](../cllocationmanager/startupdatingheading%28%29.md) method.

The location manager object calls this method after you initially start the heading service. Subsequent events are delivered when the previously reported value changes by more than the value specified in the [`headingFilter`](../cllocationmanager/headingfilter.md) property of the location manager object.

## Parameters

- `manager`: The location manager object that generated the update event.
- `newHeading`: The new heading data.

## See Also

### Receiving heading updates
- [func locationManagerShouldDisplayHeadingCalibration(CLLocationManager) -> Bool](./locationmanagershoulddisplayheadingcalibration%28_%29.md)
  Asks the delegate whether the heading calibration alert should be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didupdateheading:))*