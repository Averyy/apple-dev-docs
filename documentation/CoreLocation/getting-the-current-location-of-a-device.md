# Getting the current location of a device

**Framework**: Core Location

Start location services and provide information the system needs to optimize power usage for those services.

#### Overview

Core Location offers many different services for getting location-related data, but the most common services return the device’s current location. You might use this information to:

- Facilitate navigation, either by foot, car, or other modes of transportation.
- Identify nearby points of interest.
- Filter search results based on proximity to the person.
- Display the person’s location on a map.
- Share the person’s location with a friend.
- Tag the location of a photo.
- Check in with social media.
- Track the path someone takes during a workout or hike.

Core Location can determine the current location using many different types of hardware, including Wi-Fi, cellular, and GPS radios. Core Location doesn’t need every one of these radios to determine the location. Instead, it selectively enables radios to get the required location data in the most power-efficient way possible. The configuration of your [`CLLocationManager`](cllocationmanager.md) object affects which radios the system uses and your app’s power consumption.

##### Start the Service That Delivers the Location Data You Need

Always choose the most power-efficient location service that meets the needs of your app. Core Location provides the following services for getting location data:

- The  location service provides the most power-efficient way to get location data. The system monitors the places someone visits and the time they spend there, and delivers that data at a later time. Call [`startMonitoringVisits()`](cllocationmanager/startmonitoringvisits().md) to start the service.
- The  location service offers a low-power way to get location updates. This service uses the cellular and Wi-Fi radios (not GPS) to report only location changes that exceed a significantly large distance. Call [`startMonitoringSignificantLocationChanges()`](cllocationmanager/startmonitoringsignificantlocationchanges().md) to start the service.
- The  location service provides the most precise and regular location data, but uses more power than the other services. Use it primarily if your app provides turn-by-turn navigation or needs a greater precision or frequency of events. This location service is the only one available to apps running in visionOS. Call [`startUpdatingLocation()`](cllocationmanager/startupdatinglocation().md) to start the service, or call [`requestLocation()`](cllocationmanager/requestlocation().md) to get a single location event.

Few apps need to start location services right away, and fewer still need to keep those services running for extended periods of time. Delay the start of location services until someone interacts with your app in a way that requires that information. Then, as soon as you have the location data you need, stop services to preserve battery life. For example, stop services if you only need the current location to filter search results once.

When adding support for a location service, make sure to implement all of the service’s relevant methods in your delegate object. The Standard and Significant-change location services use the same set of delegate methods, but the Visits service has a separate method to receive visit-specific data.

For information about the behavior of individual services and how to start and stop them, see [`CLLocationManager`](cllocationmanager.md).

##### Enable Power Saving Features

Core Location optimizes power usage as much as possible, but you can still help. The best optimization is to turn off location services when your app doesn’t need new location data. Other optimizations require you to adjust the configuration of your location manager object:

- Set the [`distanceFilter`](cllocationmanager/distancefilter.md) property to the largest possible value that gives you the information you need. Higher values let the system turn off radio hardware more frequently.
- Set the [`desiredAccuracy`](cllocationmanager/desiredaccuracy.md) property to the lowest possible value that gives you the information you need. Lower accuracy values let the system use more power-efficient hardware. Lower values also let the system turn off hardware sooner.
- Configure the [`activityType`](cllocationmanager/activitytype.md) property to an appropriate value, and set the [`pausesLocationUpdatesAutomatically`](cllocationmanager/pauseslocationupdatesautomatically.md) property to [`true`](https://developer.apple.com/documentation/swift/true). Core Location uses your activity type to turn off hardware automatically when conditions allow it. For example, if the activity type is [`CLActivityType.automotiveNavigation`](clactivitytype/automotivenavigation.md) and someone’s location isn’t changing, the system might turn off radio hardware until it detects new movement.
- Set the [`allowsBackgroundLocationUpdates`](cllocationmanager/allowsbackgroundlocationupdates.md) property to [`false`](https://developer.apple.com/documentation/swift/false) when you don’t actually need background location updates.

Another way to improve power usage is to add the [`NSLocationDefaultAccuracyReduced`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocationDefaultAccuracyReduced) key with the value true to your app’s `Info.plist` file. Include this key if lower-accuracy location data is sufficient for your needs. For example, an app that returns a list of restaurants within driving distance doesn’t need someone’s precise location. As needed, you can always use your location manager to request more accurate data later. However, the system displays a prompt to the device owner to grant each request you make.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/getting-the-current-location-of-a-device)*