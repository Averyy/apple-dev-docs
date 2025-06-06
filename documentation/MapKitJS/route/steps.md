# steps

**Framework**: MapKit JS  
**Kind**: property

An array of steps that compose the overall route.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute RouteStep[] steps;
```

#### Discussion

The array contains one or more [`RouteStep`](routestep.md) objects representing distinct portions of the route. Each step corresponds to a single direction to follow along the route.

## See Also

- [name](route/name.md)
  The name assigned to the route.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/route/steps)*