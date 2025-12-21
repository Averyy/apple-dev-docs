# CLLocation

**Framework**: Core Location  
**Kind**: class

The latitude, longitude, and course information reported by the system.

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
class CLLocation
```

## Mentions

- [Converting between coordinates and user-friendly place names](converting-between-coordinates-and-user-friendly-place-names.md)
- [Getting heading and course information](getting-heading-and-course-information.md)

#### Overview

A [`CLLocation`](cllocation.md) object contains the geographical location and altitude of a device, along with values indicating the accuracy of those measurements and when they were collected. In iOS, a location object also contains course information — that is, the speed and heading in which the device was moving.

Typically, you don’t create location objects yourself. After you request location updates from your [`CLLocationManager`](cllocationmanager.md) object, the system uses onboard sensors to gather location data and report that data to your app. Some services also return previously collected location data, which you can use as context to improve your services. You can always retrieve the most recently collected location from the [`location`](CLLocationManager/location.md) property of your [`CLLocationManager`](cllocationmanager.md) object. You may create location objects yourself when you want to cache custom location data or calculate the distance between two geographical coordinates.

Use [`CLLocation`](cllocation.md) objects as-is, and don’t subclass them.

## Topics

### Creating a location object
- [init(latitude: CLLocationDegrees, longitude: CLLocationDegrees)](cllocation/init(latitude:longitude:).md)
  Creates a location object with the specified latitude and longitude.
- [init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, timestamp: Date)](cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:timestamp:).md)
  Creates a location object with the specified coordinate and altitude information.
- [init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, course: CLLocationDirection, speed: CLLocationSpeed, timestamp: Date)](cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:course:speed:timestamp:).md)
  Creates a location object with the specified coordinate, altitude, and course information.
- [init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, course: CLLocationDirection, courseAccuracy: CLLocationDirectionAccuracy, speed: CLLocationSpeed, speedAccuracy: CLLocationSpeedAccuracy, timestamp: Date)](cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:course:courseaccuracy:speed:speedaccuracy:timestamp:).md)
  Creates a location object with the specified coordinate, altitude, course, and accuracy information.
- [init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, course: CLLocationDirection, courseAccuracy: CLLocationDirectionAccuracy, speed: CLLocationSpeed, speedAccuracy: CLLocationSpeedAccuracy, timestamp: Date, sourceInfo: CLLocationSourceInformation)](cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:course:courseaccuracy:speed:speedaccuracy:timestamp:sourceinfo:).md)
### Getting the location attributes
- [var coordinate: CLLocationCoordinate2D](cllocation/coordinate.md)
  The geographical coordinate information.
- [var altitude: CLLocationDistance](cllocation/altitude.md)
  The altitude above mean sea level associated with a location, measured in meters.
- [var ellipsoidalAltitude: CLLocationDistance](cllocation/ellipsoidalaltitude.md)
  The altitude as a height above the World Geodetic System 1984 (WGS84) ellipsoid, measured in meters.
- [typealias CLLocationDistance](cllocationdistance.md)
  A distance in meters from an existing location.
- [var floor: CLFloor?](cllocation/floor.md)
  The logical floor of the building in which the user is located.
- [var timestamp: Date](cllocation/timestamp.md)
  The time at which this location was determined.
- [var sourceInformation: CLLocationSourceInformation?](cllocation/sourceinformation.md)
  Information about the source that provides the location.
### Getting the location accuracy
- [var horizontalAccuracy: CLLocationAccuracy](cllocation/horizontalaccuracy.md)
  The radius of uncertainty for the location, measured in meters.
- [var verticalAccuracy: CLLocationAccuracy](cllocation/verticalaccuracy.md)
  The validity of the altitude values, and their estimated uncertainty, measured in meters.
- [typealias CLLocationAccuracy](cllocationaccuracy.md)
  The accuracy of a geographical coordinate.
### Measuring the distance between coordinates
- [func distance(from: CLLocation) -> CLLocationDistance](cllocation/distance(from:).md)
  Returns the distance (measured in meters) from the current object’s location to the specified location.
- [func getDistanceFrom(CLLocation) -> CLLocationDistance](cllocation/getdistancefrom(_:).md)
  Returns the distance (measured in meters) from the current object’s location to the specified location.
### Getting speed and course information
- [var speed: CLLocationSpeed](cllocation/speed.md)
  The instantaneous speed of the device, measured in meters per second.
- [var speedAccuracy: CLLocationSpeedAccuracy](cllocation/speedaccuracy.md)
  The accuracy of the speed value, measured in meters per second.
- [var course: CLLocationDirection](cllocation/course.md)
  The direction in which the device is traveling, measured in degrees and relative to due north.
- [var courseAccuracy: CLLocationDirectionAccuracy](cllocation/courseaccuracy.md)
  The accuracy of the course value, measured in degrees.
- [typealias CLLocationSpeed](cllocationspeed.md)
  The velocity (measured in meters per second) at which the device is moving.
- [typealias CLLocationDirection](cllocationdirection.md)
  An azimuth that is measured in degrees relative to true north.
- [typealias CLLocationSpeedAccuracy](cllocationspeedaccuracy.md)
  The accuracy of a speed.
- [typealias CLLocationDirectionAccuracy](cllocationdirectionaccuracy.md)
  The accuracy of a compass heading.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CKRecordValue](../CloudKit/CKRecordValue-c.protocol.md)
- [CKRecordValueProtocol](../CloudKit/CKRecordValueProtocol.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Getting the current location of a device](getting-the-current-location-of-a-device.md)
  Start location services and provide information the system needs to optimize power usage for those services.
- [Handling location updates in the background](handling-location-updates-in-the-background.md)
  Configure your app to receive location updates when it isn’t running in the foreground.
- [Creating a location push service extension](creating-a-location-push-service-extension.md)
  Add and configure an extension to enable your location-sharing app to access a user’s location in response to a request from another user.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocation)*