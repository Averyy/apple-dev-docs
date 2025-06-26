# init(latitude:longitude:)

**Framework**: Core Location  
**Kind**: init

Creates a location object with the specified latitude and longitude.

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
init(latitude: CLLocationDegrees, longitude: CLLocationDegrees)
```

#### Return Value

A location object initialized with the specified geographical coordinate.

#### Discussion

Use this method to create location objects that are not necessarily based on the user’s current location. Typically, you acquire location objects from your [`CLLocationManager`](cllocationmanager.md) object, which returns the user’s actual location. However, you might use this method when you want to represent any location on a map. For example, you might create an object to represent the user’s intended destination.

This method records the latitude and longitude values you provide, and it initializes other properties to appropriate default values. Specifically, this method sets the [`altitude`](cllocation/altitude.md) and [`horizontalAccuracy`](cllocation/horizontalaccuracy.md) properties to 0, sets the [`verticalAccuracy`](cllocation/verticalaccuracy.md) property to `-1` to indicate that the altitude is invalid, sets the [`speed`](cllocation/speed.md) and [`course`](cllocation/course.md) values to `-1`, and sets the [`timestamp`](cllocation/timestamp.md) property to the time at which the returned object was created.

## Parameters

- `latitude`: The latitude of the geographical coordinate.
- `longitude`: The longitude of the geographical coordinate.

## See Also

- [init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, timestamp: Date)](cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:timestamp:).md)
  Creates a location object with the specified coordinate and altitude information.
- [init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, course: CLLocationDirection, speed: CLLocationSpeed, timestamp: Date)](cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:course:speed:timestamp:).md)
  Creates a location object with the specified coordinate, altitude, and course information.
- [init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, course: CLLocationDirection, courseAccuracy: CLLocationDirectionAccuracy, speed: CLLocationSpeed, speedAccuracy: CLLocationSpeedAccuracy, timestamp: Date)](cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:course:courseaccuracy:speed:speedaccuracy:timestamp:).md)
  Creates a location object with the specified coordinate, altitude, course, and accuracy information.
- [init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, course: CLLocationDirection, courseAccuracy: CLLocationDirectionAccuracy, speed: CLLocationSpeed, speedAccuracy: CLLocationSpeedAccuracy, timestamp: Date, sourceInfo: CLLocationSourceInformation)](cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:course:courseaccuracy:speed:speedaccuracy:timestamp:sourceinfo:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocation/init(latitude:longitude:))*