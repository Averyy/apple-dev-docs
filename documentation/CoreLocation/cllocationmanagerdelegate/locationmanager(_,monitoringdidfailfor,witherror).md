# locationManager(_:monitoringDidFailFor:withError:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a region monitoring error occurred.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
optional func locationManager(_ manager: CLLocationManager, monitoringDidFailFor region: CLRegion?, withError error: any Error)
```

```objc
- (void) locationManager:(CLLocationManager *) manager monitoringDidFailForRegion:(CLRegion *) region withError:(NSError *) error;
```

#### Discussion

If an error occurs while trying to monitor a given region, the location manager sends this message to its delegate. Region monitoring might fail because the region itself cannot be monitored or because there was a more general failure in configuring the region monitoring service.

Although implementation of this method is optional, it is recommended that you implement it if you use region monitoring in your application.

## Parameters

- `manager`: The location manager object reporting the event.
- `region`: The region for which the error occurred.
- `error`: An error object containing the error code that indicates why region monitoring failed.

## See Also

### Related documentation
- [func locationManager(CLLocationManager, didFailWithError: any Error)](./locationmanager%28_,didfailwitherror%29.md)
  Tells the delegate that the location manager was unable to retrieve a location value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:monitoringdidfailfor:witherror:))*