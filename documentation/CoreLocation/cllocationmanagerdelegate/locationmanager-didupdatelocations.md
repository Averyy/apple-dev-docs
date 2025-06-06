# locationManager(_:didUpdateLocations:)

**Framework**: Core Location  
**Kind**: method

Tells the delegate that new location data is available.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation])
```

## Mentions

- [Creating a location push service extension](creating-a-location-push-service-extension.md)

#### Discussion

Implementation of this method is optional but recommended.

## Parameters

- `manager`: The location manager object that generated the update event.
- `locations`: An array of   objects containing the location data. This array always contains at least one object representing the current location. If updates were deferred or if multiple locations arrived before they could be delivered, the array may contain additional entries. The objects in the array are organized in the order in which they occurred. Therefore, the most recent location update is at the end of the array.

## Topics

### Related Documentation
- [MapKit](../MapKit/MapKit.md)
  Display map or satellite imagery within your app, call out points of interest, and determine placemark information for map coordinates.
- [MapKit JS](../MapKitJS/MapKitJS.md)
  Embed interactive Apple Maps on your website, annotate points of interest, and perform georelated searches.

## See Also

- [func locationManager(CLLocationManager, didUpdateTo: CLLocation, from: CLLocation)](cllocationmanagerdelegate/locationmanager(_:didupdateto:from:).md)
  Tells the delegate that a new location value is available.
- [func locationManager(CLLocationManager, didFinishDeferredUpdatesWithError: (any Error)?)](cllocationmanagerdelegate/locationmanager(_:didfinishdeferredupdateswitherror:).md)
  Tells the delegate that updates will no longer be deferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didupdatelocations:))*