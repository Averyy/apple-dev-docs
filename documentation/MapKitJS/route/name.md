# name

**Framework**: MapKit JS  
**Kind**: property

The name assigned to the route.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute string name;
```

#### Discussion

Display [`name`](route/name.md) to the user so they can distinguish one route from another. MapKit JS localizes this string according to the [`mapkit.Directions`](mapkit.directions.md) object’s [`language`](directionsconstructoroptions/language.md) value.

## See Also

- [steps](route/steps.md)
  An array of steps that compose the overall route.
- [distance](route/distance.md)
  The route distance, in meters.
- [expectedTravelTime](route/expectedtraveltime.md)
  The expected travel time, in seconds.
- [transportType](route/transporttype.md)
  The overall route transport type.
- [hasTolls](route/hastolls.md)
  A Boolean value that indicates whether a route has tolls.
- [mapkit.Directions.Transport](mapkit.directions.transport.md)
  The modes of transportation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/route/name)*