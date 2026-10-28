# MKMetersPerMapPointAtLatitude(_:)

**Framework**: MapKit  
**Kind**: func  
**Role**: Function

Returns the distance that one map point spans at the specified latitude.

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
func MKMetersPerMapPointAtLatitude(_ latitude: CLLocationDegrees) -> CLLocationDistance
```

```c
extern CLLocationDistance MKMetersPerMapPointAtLatitude(CLLocationDegrees latitude);
```

## Return Value

The distance (in meters) spanned by a single map point.

## Discussion

The distance between map points decreases as the latitude approaches the poles. This relationship parallels the relationship between longitudinal coordinates at different latitudes.

## Parameters

- `latitude`: The latitude for which to return the value.

## See Also

### Getting the distance between points
- [func distance(to: MKMapPoint) -> CLLocationDistance](./mkmappoint/distance%28to%29.md)
  Returns the number of meters between two map points.
- [func MKMapPointsPerMeterAtLatitude(CLLocationDegrees) -> Double](./mkmappointspermeteratlatitude%28_%29.md)
  Returns the number of map points that represent one meter at the specified latitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmeterspermappointatlatitude(_:))*