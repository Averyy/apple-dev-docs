# init(coordinate:altitude:horizontalAccuracy:verticalAccuracy:timestamp:)

**Framework**: Core Location  
**Kind**: init  
**Role**: Initializer

Creates a location object with the specified coordinate and altitude information.

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
init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, timestamp: Date)
```

```objc
- (instancetype) initWithCoordinate:(CLLocationCoordinate2D) coordinate altitude:(CLLocationDistance) altitude horizontalAccuracy:(CLLocationAccuracy) hAccuracy verticalAccuracy:(CLLocationAccuracy) vAccuracy timestamp:(NSDate *) timestamp;
```

#### Return Value

A location object initialized with the specified geographical coordinate and altitude information.

#### Discussion

Use this method to create location objects that are not necessarily based on the user’s current location.Typically, you acquire location objects from your [`CLLocationManager`](../cllocationmanager.md) object, which returns the user’s actual location. However, you might use this method when you want to represent any location on a map. For example, you might create an object to represent the user’s intended destination.

This method records the values you provide, and it initializes other properties to appropriate default values. Specifically, this method sets the speed and course values to `-1`.

## Parameters

- `coordinate`: A coordinate structure containing the latitude and longitude values.
- `altitude`: The altitude value for the location.
- `hAccuracy`: The radius of uncertainty for the geographical coordinate, measured in meters. Specify a negative number to indicate that the geographical coordinate is invalid.
- `vAccuracy`: The accuracy of the altitude value, measured in meters. Specify a negative number to indicate that the altitude is invalid.
- `timestamp`: The time to associate with the location object. Typically, you specify the current time.

## See Also

### Creating a location object
- [init(latitude: CLLocationDegrees, longitude: CLLocationDegrees)](./init%28latitude,longitude%29.md)
  Creates a location object with the specified latitude and longitude.
- [init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, course: CLLocationDirection, speed: CLLocationSpeed, timestamp: Date)](./init%28coordinate,altitude,horizontalaccuracy,verticalaccuracy,course,speed,timestamp%29.md)
  Creates a location object with the specified coordinate, altitude, and course information.
- [init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, course: CLLocationDirection, courseAccuracy: CLLocationDirectionAccuracy, speed: CLLocationSpeed, speedAccuracy: CLLocationSpeedAccuracy, timestamp: Date)](./init%28coordinate,altitude,horizontalaccuracy,verticalaccuracy,course,courseaccuracy,speed,speedaccuracy,timestamp%29.md)
  Creates a location object with the specified coordinate, altitude, course, and accuracy information.
- [init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, course: CLLocationDirection, courseAccuracy: CLLocationDirectionAccuracy, speed: CLLocationSpeed, speedAccuracy: CLLocationSpeedAccuracy, timestamp: Date, sourceInfo: CLLocationSourceInformation)](./init%28coordinate,altitude,horizontalaccuracy,verticalaccuracy,course,courseaccuracy,speed,speedaccuracy,timestamp,sourceinfo%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:timestamp:))*