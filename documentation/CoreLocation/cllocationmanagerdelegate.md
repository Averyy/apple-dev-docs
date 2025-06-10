# CLLocationManagerDelegate

**Framework**: Core Location  
**Kind**: protocol

The methods you use to receive events from an associated location-manager object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol CLLocationManagerDelegate : NSObjectProtocol
```

#### Overview

The location manager calls its delegate’s methods to report location-related events to your app. Implement this protocol in an app-specific object and use the methods to update your app. For example, you might use the current location to update the user’s position on a map or you might return search results relevant only to the user’s current location.

> ❗ **Important**:  Always implement the methods for handling any potential failures in addition to the methods for receiving location-related data.

Assign your delegate object to the [`delegate`](cllocationmanager/delegate.md) property of the [`CLLocationManager`](cllocationmanager.md) object before starting any services. Core Location may report a cached value to your delegate immediately after you start the service, followed by a more current value later. Check the time stamp of any data objects you receive before using them.

Core Location calls the methods of your delegate object on the runloop from the thread on which you initialized [`CLLocationManager`](cllocationmanager.md). That thread must itself have an active run loop, like the one found in your app’s main thread.

## Topics

### Responding to authorization changes
- [func locationManagerDidChangeAuthorization(CLLocationManager)](cllocationmanagerdelegate/locationmanagerdidchangeauthorization(_:).md)
  Tells the delegate when the app creates the location manager and when the authorization status changes.
- [func locationManager(CLLocationManager, didChangeAuthorization: CLAuthorizationStatus)](cllocationmanagerdelegate/locationmanager(_:didchangeauthorization:).md)
  Tells the delegate its authorization status when the app creates the location manager and when the authorization status changes.
### Handling errors
- [func locationManager(CLLocationManager, didFailWithError: any Error)](cllocationmanagerdelegate/locationmanager(_:didfailwitherror:).md)
  Tells the delegate that the location manager was unable to retrieve a location value.
### Receiving location updates
- [func locationManager(CLLocationManager, didUpdateLocations: [CLLocation])](cllocationmanagerdelegate/locationmanager(_:didupdatelocations:).md)
  Tells the delegate that new location data is available.
- [func locationManager(CLLocationManager, didUpdateTo: CLLocation, from: CLLocation)](cllocationmanagerdelegate/locationmanager(_:didupdateto:from:).md)
  Tells the delegate that a new location value is available.
- [func locationManager(CLLocationManager, didFinishDeferredUpdatesWithError: (any Error)?)](cllocationmanagerdelegate/locationmanager(_:didfinishdeferredupdateswitherror:).md)
  Tells the delegate that updates will no longer be deferred.
### Pausing location updates
- [func locationManagerDidPauseLocationUpdates(CLLocationManager)](cllocationmanagerdelegate/locationmanagerdidpauselocationupdates(_:).md)
  Tells the delegate that location updates were paused.
- [func locationManagerDidResumeLocationUpdates(CLLocationManager)](cllocationmanagerdelegate/locationmanagerdidresumelocationupdates(_:).md)
  Tells the delegate that the delivery of location updates has resumed.
### Receiving visit updates
- [func locationManager(CLLocationManager, didVisit: CLVisit)](cllocationmanagerdelegate/locationmanager(_:didvisit:).md)
  Tells the delegate that a new visit-related event was received.
### Receiving heading updates
- [func locationManager(CLLocationManager, didUpdateHeading: CLHeading)](cllocationmanagerdelegate/locationmanager(_:didupdateheading:).md)
  Tells the delegate that the location manager received updated heading information.
- [func locationManagerShouldDisplayHeadingCalibration(CLLocationManager) -> Bool](cllocationmanagerdelegate/locationmanagershoulddisplayheadingcalibration(_:).md)
  Asks the delegate whether the heading calibration alert should be displayed.
### Receiving region-related updates
- [func locationManager(CLLocationManager, didEnterRegion: CLRegion)](cllocationmanagerdelegate/locationmanager(_:didenterregion:).md)
  Tells the delegate that the user entered the specified region.
- [func locationManager(CLLocationManager, didExitRegion: CLRegion)](cllocationmanagerdelegate/locationmanager(_:didexitregion:).md)
  Tells the delegate that the user left the specified region.
- [func locationManager(CLLocationManager, didDetermineState: CLRegionState, for: CLRegion)](cllocationmanagerdelegate/locationmanager(_:diddeterminestate:for:).md)
  Tells the delegate about the state of the specified region.
- [func locationManager(CLLocationManager, monitoringDidFailFor: CLRegion?, withError: any Error)](cllocationmanagerdelegate/locationmanager(_:monitoringdidfailfor:witherror:).md)
  Tells the delegate that a region monitoring error occurred.
- [func locationManager(CLLocationManager, didStartMonitoringFor: CLRegion)](cllocationmanagerdelegate/locationmanager(_:didstartmonitoringfor:).md)
  Tells the delegate that a new region is being monitored.
- [enum CLRegionState](clregionstate.md)
  Constants that reflect the relationship of the current location to the region boundaries.
### Receiving beacon-related updates
- [func locationManager(CLLocationManager, didRange: [CLBeacon], satisfying: CLBeaconIdentityConstraint)](cllocationmanagerdelegate/locationmanager(_:didrange:satisfying:).md)
  Tells the delegate that the location manager detected at least one beacon that satisfies the provided constraint.
- [func locationManager(CLLocationManager, didFailRangingFor: CLBeaconIdentityConstraint, error: any Error)](cllocationmanagerdelegate/locationmanager(_:didfailrangingfor:error:).md)
  Tells the delegate that the location manager couldn’t detect any beacons that satisfy the provided constraint.
- [func locationManager(CLLocationManager, didRangeBeacons: [CLBeacon], in: CLBeaconRegion)](cllocationmanagerdelegate/locationmanager(_:didrangebeacons:in:).md)
  Tells the delegate that one or more beacons are in range.
- [func locationManager(CLLocationManager, rangingBeaconsDidFailFor: CLBeaconRegion, withError: any Error)](cllocationmanagerdelegate/locationmanager(_:rangingbeaconsdidfailfor:witherror:).md)
  Tells the delegate that an error occurred while gathering ranging information for a set of beacons.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any CLLocationManagerDelegate)?](cllocationmanager/delegate.md)
  The delegate object to receive update events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate)*