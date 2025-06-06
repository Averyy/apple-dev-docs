# distance

**Framework**: MapKit JS  
**Kind**: property

The route distance, in meters.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute number distance;
```

#### Discussion

This property reflects the distance that the user covers while traversing the path of the route. It isn’t a straight line distance between the [`origin`](directionsrequest/origin.md) and [`destination`](directionsrequest/destination.md).

## See Also

- [steps](route/steps.md)
  An array of steps that compose the overall route.
- [name](route/name.md)
  The name assigned to the route.
- [expectedTravelTime](route/expectedtraveltime.md)
  The expected travel time, in seconds.
- [transportType](route/transporttype.md)
  The overall route transport type.
- [hasTolls](route/hastolls.md)
  A Boolean value that indicates whether a route has tolls.
- [mapkit.Directions.Transport](mapkit.directions.transport.md)
  The modes of transportation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/route/distance)*