# Core Location

**Framework**: Core Location  
**Kind**: module

Obtain the geographic location and orientation of a device.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

#### Overview

Core Location provides services that determine a device’s geographic location, altitude, and orientation, or its position relative to a nearby iBeacon device. The framework gathers data using all available components on the device, including the Wi-Fi, GPS, Bluetooth, magnetometer, barometer, and cellular hardware.

You use instances of the [`CLLocationManager`](cllocationmanager.md) class to configure, start, and stop the Core Location services. A location manager object supports the following location-related activities:

To use location services, call [`liveUpdates(_:)`](cllocationupdate/liveupdates(_:).md) to obtain an update stream, then asynchronously iterate over that stream to receive and process location updates, and receive diagnostic properties to understand if and why location updates don’t arrive.

If needed, the system prompts the user to grant or deny the request. An initial prompt is shown in the example below:

![A screenshot of an iPhone showing a prompt asking the user if they allow the “Park Finder” app to have access to their location. The options are “OK” and “Not now”.](https://docs-assets.developer.apple.com/published/71e6a0fc9cb93b0e6926165d35fc2b16/core-location-overview%402x.png)

On iOS devices, users can change location service settings at any time in the Settings app, affecting individual apps or the device as a whole. Your app receives events, including authorization changes, by observing asynchronous sequences from [`CLLocationUpdate`](cllocationupdate.md) and [`CLMonitor`](clmonitor-6ynwz.md).

## Topics

### Essentials
- [Configuring your app to use location services](configuring-your-app-to-use-location-services.md)
  Prepare your app to start collecting location data.
- [Supporting live updates in SwiftUI and Mac Catalyst apps](supporting-live-updates-in-swiftui-and-mac-catalyst-apps.md)
  Enable background events by adding lifecycle event support.
- [class CLLocationManager](cllocationmanager.md)
  The object you use to start and stop the delivery of location-related events to your app.
- [class CLBackgroundActivitySession](clbackgroundactivitysession-3mzv3.md)
  An object that manages a visual indicator that keeps your app in use in the background, allowing it to receive updates or events.
- [struct CLLocationUpdate](cllocationupdate.md)
  A structure that contains the location information the framework delivers with each update.
- [Adopting live updates in Core Location](adopting-live-updates-in-core-location.md)
  Simplify location delivery using asynchronous events in Swift.
- [Monitoring location changes with Core Location](monitoring-location-changes-with-core-location.md)
  Define boundaries and act on user location updates.
### Authorization
- [Requesting authorization to use location services](requesting-authorization-to-use-location-services.md)
  Obtain authorization to use location services and manage changes to your app’s authorization status.
- [Suspending authorization requests](suspending-authorization-requests.md)
  Defer the system’s authorization request dialog until your app is ready.
- [enum CLAuthorizationStatus](clauthorizationstatus.md)
  Constants that indicate the app’s authorization to use location services.
- [enum CLAccuracyAuthorization](claccuracyauthorization.md)
  Constants that indicate the level of location accuracy the app has authorization to use.
- [NSLocationAlwaysAndWhenInUseUsageDescription](../BundleResources/Information-Property-List/NSLocationAlwaysAndWhenInUseUsageDescription.md)
  A message that tells the user why the app is requesting access to the user’s location information at all times.
- [NSLocationWhenInUseUsageDescription](../BundleResources/Information-Property-List/NSLocationWhenInUseUsageDescription.md)
  A message that tells the user why the app is requesting access to the user’s location information while the app is running in the foreground.
- [NSLocationUsageDescription](../BundleResources/Information-Property-List/NSLocationUsageDescription.md)
  A message that tells the user why the app is requesting access to the user’s location information.
- [NSLocationDefaultAccuracyReduced](../BundleResources/Information-Property-List/NSLocationDefaultAccuracyReduced.md)
  A Boolean value that indicates whether the app requests reduced location accuracy by default.
- [NSLocationAlwaysUsageDescription](../BundleResources/Information-Property-List/NSLocationAlwaysUsageDescription.md)
  A message that tells the user why the app is requesting access to the user’s location at all times.
### Monitoring
- [actor CLMonitor](clmonitor-2r51v.md)
  An object that monitors the conditions you add to it.
### Location updates
- [Getting the current location of a device](getting-the-current-location-of-a-device.md)
  Start location services and provide information the system needs to optimize power usage for those services.
- [Handling location updates in the background](handling-location-updates-in-the-background.md)
  Configure your app to receive location updates when it isn’t running in the foreground.
- [Creating a location push service extension](creating-a-location-push-service-extension.md)
  Add and configure an extension to enable your location-sharing app to access a user’s location in response to a request from another user.
- [class CLLocation](cllocation.md)
  The latitude, longitude, and course information reported by the system.
- [struct CLLocationCoordinate2D](cllocationcoordinate2d.md)
  The latitude and longitude associated with a location, specified using the WGS 84 reference frame.
- [class CLFloor](clfloor.md)
  The floor of a building on which the user’s device is located.
- [class CLVisit](clvisit.md)
  Information about the user’s location during a specific period of time.
- [class CLLocationSourceInformation](cllocationsourceinformation.md)
  Information about the source that provides a location.
- [Monitoring location changes with Core Location](monitoring-location-changes-with-core-location.md)
  Define boundaries and act on user location updates.
- [class CLServiceSession](clservicesession-pt7n.md)
### Region monitoring
- [Monitoring the user’s proximity to geographic regions](monitoring-the-user-s-proximity-to-geographic-regions.md)
  Use condition monitoring to determine when the user enters or leaves a geographic region.
- [class CLRegion](clregion.md)
  A base class representing an area that can be monitored.
### iBeacon
- [Ranging for Beacons](ranging-for-beacons.md)
  Configure a device to act as a beacon and to detect surrounding beacons.
- [Determining the proximity to an iBeacon device](determining-the-proximity-to-an-ibeacon-device.md)
  Detect beacons and determine the relative distance to them.
- [Turning an iOS device into an iBeacon device](turning-an-ios-device-into-an-ibeacon-device.md)
  Broadcast iBeacon signals from an iOS device.
- [class CLBeacon](clbeacon.md)
  Information about an observed iBeacon device and its relative distance to a person’s device.
- [protocol CLCondition](clcondition-swift.protocol.md)
  The abstract base class for all other monitor conditions.
### Compass headings
- [Getting heading and course information](getting-heading-and-course-information.md)
  Use a device’s orientation and course information for navigation.
- [class CLHeading](clheading.md)
  The orientation of the user’s device, relative to true or magnetic north.
### Geocoding
- [Converting between coordinates and user-friendly place names](converting-between-coordinates-and-user-friendly-place-names.md)
  Convert between a latitude and longitude pair and a more user-friendly description of that location.
- [Converting a user’s location to a descriptive placemark](converting-a-user-s-location-to-a-descriptive-placemark.md)
  Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.
- [class CLGeocoder](clgeocoder.md)
  An interface for converting between geographic coordinates and place names.
- [class CLPlacemark](clplacemark.md)
  A user-friendly description of a geographic coordinate, often containing the name of the place, its address, and other relevant information.
### Location push service extension
- [com.apple.developer.location.push](../BundleResources/Entitlements/com.apple.developer.location.push.md)
  An entitlement to enable a location-sharing app to query someone’s location in response to a push notification.
- [protocol CLLocationPushServiceExtension](cllocationpushserviceextension.md)
  The interface you adopt in the type that acts as the main entry point for a Location Push Service Extension.
- [struct CLLocationPushServiceError](cllocationpushserviceerror-swift.struct.md)
  Error codes the location manager returns if starting to monitor for location push notifications fails.
- [let CLLocationPushServiceErrorDomain: String](cllocationpushserviceerrordomain.md)
  The domain for Location Push Service Extension errors.
- [CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/code.md)
  Error codes the location manager returns if starting to monitor for location push notifications fails.
### Errors
- [struct CLError](clerror-swift.struct.md)
  A Core Location error.
- [let kCLErrorDomain: String](kclerrordomain.md)
  The domain for Core Location errors.
- [let kCLErrorUserInfoAlternateRegionKey: String](kclerroruserinfoalternateregionkey.md)
  A key in the user information dictionary of an error relating to a delayed region-monitoring response.
### Deprecated
- [Deprecated](deprecated.md)
### Reference
- [Core Location Constants](core-location-constants.md)
  This document describes the constants found in the Core Location framework.
- [Core Location Functions](core-location-functions.md)
  The Core Location framework provides functions to help you work with coordinate values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreLocation)*