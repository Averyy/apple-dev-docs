# init(coordinate:altitude:horizontalAccuracy:verticalAccuracy:course:speed:timestamp:)

**Framework**: Core Location  
**Kind**: init

Creates a location object with the specified coordinate, altitude, and course information.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, course: CLLocationDirection, speed: CLLocationSpeed, timestamp: Date)
```

#### Return Value

A location object initialized with the specified geographical coordinate, altitude, and course information.

#### Discussion

Use this method to create location objects that aren’t necessarily based on the user’s current location.Typically, you acquire location objects from your [`CLLocationManager`](cllocationmanager.md) object, which returns the user’s actual location. However, you might use this method when you want to represent any location on a map. For example, you might create an object to represent the user’s intended destination.

## Parameters

- `coordinate`: A coordinate structure containing the latitude and longitude values.
- `altitude`: The altitude value for the location.
- `hAccuracy`: The radius of uncertainty for the geographical coordinate, measured in meters. Specify a negative number to indicate that the geographical coordinate is invalid.
- `vAccuracy`: The accuracy of the altitude value, measured in meters. Specify a negative number to indicate that the altitude is invalid.
- `course`: The direction of travel for the location, measured in degrees relative to due north and continuing clockwise around the compass.
- `speed`: The current speed associated with this location, measured in meters per second.
- `timestamp`: The time to associate with the location object. Typically, you specify the current time.

## See Also

- [init(latitude: CLLocationDegrees, longitude: CLLocationDegrees)](cllocation/init(latitude:longitude:).md)
  Creates a location object with the specified latitude and longitude.
- [init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, timestamp: Date)](cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:timestamp:).md)
  Creates a location object with the specified coordinate and altitude information.
- [init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, course: CLLocationDirection, courseAccuracy: CLLocationDirectionAccuracy, speed: CLLocationSpeed, speedAccuracy: CLLocationSpeedAccuracy, timestamp: Date)](cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:course:courseaccuracy:speed:speedaccuracy:timestamp:).md)
  Creates a location object with the specified coordinate, altitude, course, and accuracy information.
- [init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, course: CLLocationDirection, courseAccuracy: CLLocationDirectionAccuracy, speed: CLLocationSpeed, speedAccuracy: CLLocationSpeedAccuracy, timestamp: Date, sourceInfo: CLLocationSourceInformation)](cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:course:courseaccuracy:speed:speedaccuracy:timestamp:sourceinfo:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:course:speed:timestamp:))*