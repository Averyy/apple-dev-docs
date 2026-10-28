# CLLocationManagerDelegate

**Framework**: Core Location  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol CLLocationManagerDelegate <NSObject>
```

## Overview

The location manager calls its delegate’s methods to report location-related events to your app. Implement this protocol in an app-specific object and use the methods to update your app. For example, you might use the current location to update the user’s position on a map or you might return search results relevant only to the user’s current location.

> ❗ **Important**:  Always implement the methods for handling any potential failures in addition to the methods for receiving location-related data.

Assign your delegate object to the [`delegate`](./cllocationmanager/delegate.md) property of the [`CLLocationManager`](./cllocationmanager.md) object before starting any services. Core Location may report a cached value to your delegate immediately after you start the service, followed by a more current value later. Check the time stamp of any data objects you receive before using them.

Core Location calls the methods of your delegate object on the runloop from the thread on which you initialized [`CLLocationManager`](./cllocationmanager.md). That thread must itself have an active run loop, like the one found in your app’s main thread.

## Topics

### Responding to authorization changes
- [func locationManagerDidChangeAuthorization(CLLocationManager)](./cllocationmanagerdelegate/locationmanagerdidchangeauthorization%28_%29.md)
  Tells the delegate when the app creates the location manager and when the authorization status changes.
- [func locationManager(CLLocationManager, didChangeAuthorization: CLAuthorizationStatus)](./cllocationmanagerdelegate/locationmanager%28_,didchangeauthorization%29.md)
  Tells the delegate its authorization status when the app creates the location manager and when the authorization status changes.
### Handling errors
- [func locationManager(CLLocationManager, didFailWithError: any Error)](./cllocationmanagerdelegate/locationmanager%28_,didfailwitherror%29.md)
  Tells the delegate that the location manager was unable to retrieve a location value.
### Receiving location updates
- [func locationManager(CLLocationManager, didUpdateLocations: [CLLocation])](./cllocationmanagerdelegate/locationmanager%28_,didupdatelocations%29.md)
  Tells the delegate that new location data is available.
- [func locationManager(CLLocationManager, didUpdateTo: CLLocation, from: CLLocation)](./cllocationmanagerdelegate/locationmanager%28_,didupdateto,from%29.md)
  Tells the delegate that a new location value is available.
- [func locationManager(CLLocationManager, didFinishDeferredUpdatesWithError: (any Error)?)](./cllocationmanagerdelegate/locationmanager%28_,didfinishdeferredupdateswitherror%29.md)
  Tells the delegate that updates will no longer be deferred.
### Pausing location updates
- [func locationManagerDidPauseLocationUpdates(CLLocationManager)](./cllocationmanagerdelegate/locationmanagerdidpauselocationupdates%28_%29.md)
  Tells the delegate that location updates were paused.
- [func locationManagerDidResumeLocationUpdates(CLLocationManager)](./cllocationmanagerdelegate/locationmanagerdidresumelocationupdates%28_%29.md)
  Tells the delegate that the delivery of location updates has resumed.
### Receiving visit updates
- [func locationManager(CLLocationManager, didVisit: CLVisit)](./cllocationmanagerdelegate/locationmanager%28_,didvisit%29.md)
  Tells the delegate that a new visit-related event was received.
### Receiving heading updates
- [func locationManager(CLLocationManager, didUpdateHeading: CLHeading)](./cllocationmanagerdelegate/locationmanager%28_,didupdateheading%29.md)
  Tells the delegate that the location manager received updated heading information.
- [func locationManagerShouldDisplayHeadingCalibration(CLLocationManager) -> Bool](./cllocationmanagerdelegate/locationmanagershoulddisplayheadingcalibration%28_%29.md)
  Asks the delegate whether the heading calibration alert should be displayed.
### Receiving region-related updates
- [func locationManager(CLLocationManager, didEnterRegion: CLRegion)](./cllocationmanagerdelegate/locationmanager%28_,didenterregion%29.md)
  Tells the delegate that the user entered the specified region.
- [func locationManager(CLLocationManager, didExitRegion: CLRegion)](./cllocationmanagerdelegate/locationmanager%28_,didexitregion%29.md)
  Tells the delegate that the user left the specified region.
- [func locationManager(CLLocationManager, didDetermineState: CLRegionState, for: CLRegion)](./cllocationmanagerdelegate/locationmanager%28_,diddeterminestate,for%29.md)
  Tells the delegate about the state of the specified region.
- [func locationManager(CLLocationManager, monitoringDidFailFor: CLRegion?, withError: any Error)](./cllocationmanagerdelegate/locationmanager%28_,monitoringdidfailfor,witherror%29.md)
  Tells the delegate that a region monitoring error occurred.
- [func locationManager(CLLocationManager, didStartMonitoringFor: CLRegion)](./cllocationmanagerdelegate/locationmanager%28_,didstartmonitoringfor%29.md)
  Tells the delegate that a new region is being monitored.
- [enum CLRegionState](./clregionstate.md)
  Constants that reflect the relationship of the current location to the region boundaries.
### Receiving beacon-related updates
- [func locationManager(CLLocationManager, didRange: [CLBeacon], satisfying: CLBeaconIdentityConstraint)](./cllocationmanagerdelegate/locationmanager%28_,didrange,satisfying%29.md)
  Tells the delegate that the location manager detected at least one beacon that satisfies the provided constraint.
- [func locationManager(CLLocationManager, didFailRangingFor: CLBeaconIdentityConstraint, error: any Error)](./cllocationmanagerdelegate/locationmanager%28_,didfailrangingfor,error%29.md)
  Tells the delegate that the location manager couldn’t detect any beacons that satisfy the provided constraint.
- [func locationManager(CLLocationManager, didRangeBeacons: [CLBeacon], in: CLBeaconRegion)](./cllocationmanagerdelegate/locationmanager%28_,didrangebeacons,in%29.md)
  Tells the delegate that one or more beacons are in range.
- [func locationManager(CLLocationManager, rangingBeaconsDidFailFor: CLBeaconRegion, withError: any Error)](./cllocationmanagerdelegate/locationmanager%28_,rangingbeaconsdidfailfor,witherror%29.md)
  Tells the delegate that an error occurred while gathering ranging information for a set of beacons.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Receiving data from location services
- [var delegate: (any CLLocationManagerDelegate)?](./cllocationmanager/delegate.md)
  The delegate object to receive update events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate)*