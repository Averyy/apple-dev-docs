# MKMapPointsPerMeterAtLatitude(_:)

**Framework**: MapKit  
**Kind**: func  
**Role**: Function

Returns the number of map points that represent one meter at the specified latitude.

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
func MKMapPointsPerMeterAtLatitude(_ latitude: CLLocationDegrees) -> Double
```

```c
extern double MKMapPointsPerMeterAtLatitude(CLLocationDegrees latitude);
```

## Return Value

The number of map points that span one meter.

## Discussion

The number of map points per meter increases as the latitude approaches the poles.

## Parameters

- `latitude`: The latitude for which to return the value.

## See Also

### Getting the distance between points
- [func distance(to: MKMapPoint) -> CLLocationDistance](./mkmappoint/distance%28to%29.md)
  Returns the number of meters between two map points.
- [func MKMetersPerMapPointAtLatitude(CLLocationDegrees) -> CLLocationDistance](./mkmeterspermappointatlatitude%28_%29.md)
  Returns the distance that one map point spans at the specified latitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmappointspermeteratlatitude(_:))*