# init(coordinate:altitude:horizontalAccuracy:verticalAccuracy:course:courseAccuracy:speed:speedAccuracy:timestamp:)

**Framework**: Core Location  
**Kind**: init

Creates a location object with the specified coordinate, altitude, course, and accuracy information.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 13.4+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, course: CLLocationDirection, courseAccuracy: CLLocationDirectionAccuracy, speed: CLLocationSpeed, speedAccuracy: CLLocationSpeedAccuracy, timestamp: Date)
```

## Parameters

- `coordinate`: A coordinate structure containing the latitude and longitude values.
- `altitude`: The altitude value for the location.
- `hAccuracy`: The radius of uncertainty for the geographical coordinate, measured in meters. Specify a negative number to indicate that the geographical coordinate is invalid.
- `vAccuracy`: The accuracy of the altitude value, measured in meters. Specify a negative number to indicate that the altitude is invalid.
- `course`: The direction of travel for the location, measured in degrees relative to due north and continuing clockwise around the compass.
- `courseAccuracy`: The accuracy of the course value, measured in degrees. Specify a negative number to indicate that the course is invalid.
- `speed`: The current speed associated with this location, measured in meters per second.
- `speedAccuracy`: The accuracy of the speed value, measured in meters per second. Specify a negative number to indicate that the speed is invalid.
- `timestamp`: The time to associate with the location object. Typically, you specify the current time.

## See Also

- [init(latitude: CLLocationDegrees, longitude: CLLocationDegrees)](cllocation/init(latitude:longitude:).md)
  Creates a location object with the specified latitude and longitude.
- [init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, timestamp: Date)](cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:timestamp:).md)
  Creates a location object with the specified coordinate and altitude information.
- [init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, course: CLLocationDirection, speed: CLLocationSpeed, timestamp: Date)](cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:course:speed:timestamp:).md)
  Creates a location object with the specified coordinate, altitude, and course information.
- [init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, course: CLLocationDirection, courseAccuracy: CLLocationDirectionAccuracy, speed: CLLocationSpeed, speedAccuracy: CLLocationSpeedAccuracy, timestamp: Date, sourceInfo: CLLocationSourceInformation)](cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:course:courseaccuracy:speed:speedaccuracy:timestamp:sourceinfo:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:course:courseaccuracy:speed:speedaccuracy:timestamp:))*