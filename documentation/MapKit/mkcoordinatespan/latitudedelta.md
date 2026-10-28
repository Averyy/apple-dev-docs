# latitudeDelta

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The amount of north-to-south distance (measured in degrees) to display on the map.

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
var latitudeDelta: CLLocationDegrees
```

```c
CLLocationDegrees latitudeDelta;
```

## Discussion

Unlike longitudinal distances, which vary based on the latitude, one degree of latitude is always approximately 111 kilometers (69 miles).

## See Also

### Related Documentation
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
### Getting the span coordinates
- [var longitudeDelta: CLLocationDegrees](./longitudedelta.md)
  The amount of east-to-west distance (measured in degrees) to display for the map region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkcoordinatespan/latitudedelta)*