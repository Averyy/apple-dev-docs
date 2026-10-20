# longitudeDelta

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The amount of east-to-west distance (measured in degrees) to display for the map region.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var longitudeDelta: CLLocationDegrees
```

```c
CLLocationDegrees longitudeDelta;
```

#### Discussion

The number of kilometers spanned by a longitude range varies based on the current latitude. For example, one degree of longitude spans a distance of approximately 111 kilometers (69 miles) at the equator but shrinks to 0 kilometers at the poles.

## See Also

### Getting the span coordinates
- [var latitudeDelta: CLLocationDegrees](./latitudedelta.md)
  The amount of north-to-south distance (measured in degrees) to display on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkcoordinatespan/longitudedelta)*