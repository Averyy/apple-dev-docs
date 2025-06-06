# locationManager(_:didFailWithError:)

**Framework**: Core Location  
**Kind**: method

Tells the delegate that the location manager was unable to retrieve a location value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func locationManager(_ manager: CLLocationManager, didFailWithError error: any Error)
```

#### Discussion

If you do not implement this method, Core Location throws an exception when attempting to use location services.

The location manager calls this method when it encounters an error trying to get the location or heading data. If the location service is unable to retrieve a location right away, it reports a [`CLError.Code.locationUnknown`](clerror-swift.struct/code/locationunknown.md) error and keeps trying. In such a situation, you can simply ignore the error and wait for a new event. If a heading could not be determined because of strong interference from nearby magnetic fields, this method returns [`CLError.Code.headingFailure`](clerror-swift.struct/code/headingfailure.md).

If the user denies your app’s use of the location service, this method reports a [`CLError.Code.denied`](clerror-swift.struct/code/denied.md) error. Upon receiving such an error, you should stop the location service.

## Parameters

- `manager`: The location manager object that was unable to retrieve the location.
- `error`: The error object containing the reason the location or heading could not be retrieved.

## See Also

- [func locationManager(CLLocationManager, monitoringDidFailFor: CLRegion?, withError: any Error)](cllocationmanagerdelegate/locationmanager(_:monitoringdidfailfor:witherror:).md)
  Tells the delegate that a region monitoring error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didfailwitherror:))*