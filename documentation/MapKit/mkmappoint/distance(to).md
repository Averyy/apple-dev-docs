# distance(to:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Returns the number of meters between two map points.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func distance(to b: MKMapPoint) -> CLLocationDistance
```

```c
extern CLLocationDistance MKMetersBetweenMapPoints(MKMapPoint a, MKMapPoint b);
```

#### Return Value

The number of meters between the specified map points.

#### Discussion

This distance reflects the actual distance between the two points on the surface of the globe, taking into account the curvature of the Earth.

## Parameters

- `b`: The second map point.

## See Also

### Getting the distance between points
- [func MKMetersPerMapPointAtLatitude(CLLocationDegrees) -> CLLocationDistance](../mkmeterspermappointatlatitude%28_%29.md)
  Returns the distance that one map point spans at the specified latitude.
- [func MKMapPointsPerMeterAtLatitude(CLLocationDegrees) -> Double](../mkmappointspermeteratlatitude%28_%29.md)
  Returns the number of map points that represent one meter at the specified latitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmappoint/distance(to:))*