# init(coordinate:altitude:horizontalAccuracy:verticalAccuracy:course:courseAccuracy:speed:speedAccuracy:timestamp:sourceInfo:)

**Framework**: Core Location  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, course: CLLocationDirection, courseAccuracy: CLLocationDirectionAccuracy, speed: CLLocationSpeed, speedAccuracy: CLLocationSpeedAccuracy, timestamp: Date, sourceInfo: CLLocationSourceInformation)
```

```objc
- (instancetype) initWithCoordinate:(CLLocationCoordinate2D) coordinate altitude:(CLLocationDistance) altitude horizontalAccuracy:(CLLocationAccuracy) hAccuracy verticalAccuracy:(CLLocationAccuracy) vAccuracy course:(CLLocationDirection) course courseAccuracy:(CLLocationDirectionAccuracy) courseAccuracy speed:(CLLocationSpeed) speed speedAccuracy:(CLLocationSpeedAccuracy) speedAccuracy timestamp:(NSDate *) timestamp sourceInfo:(CLLocationSourceInformation *) sourceInfo;
```

## See Also

### Creating a location object
- [init(latitude: CLLocationDegrees, longitude: CLLocationDegrees)](./init%28latitude,longitude%29.md)
  Creates a location object with the specified latitude and longitude.
- [init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, timestamp: Date)](./init%28coordinate,altitude,horizontalaccuracy,verticalaccuracy,timestamp%29.md)
  Creates a location object with the specified coordinate and altitude information.
- [init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, course: CLLocationDirection, speed: CLLocationSpeed, timestamp: Date)](./init%28coordinate,altitude,horizontalaccuracy,verticalaccuracy,course,speed,timestamp%29.md)
  Creates a location object with the specified coordinate, altitude, and course information.
- [init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, course: CLLocationDirection, courseAccuracy: CLLocationDirectionAccuracy, speed: CLLocationSpeed, speedAccuracy: CLLocationSpeedAccuracy, timestamp: Date)](./init%28coordinate,altitude,horizontalaccuracy,verticalaccuracy,course,courseaccuracy,speed,speedaccuracy,timestamp%29.md)
  Creates a location object with the specified coordinate, altitude, course, and accuracy information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocation/init(coordinate:altitude:horizontalaccuracy:verticalaccuracy:course:courseaccuracy:speed:speedaccuracy:timestamp:sourceinfo:))*