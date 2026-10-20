# distance

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

The route distance, in meters.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
distance: number;
```

#### Discussion

This property reflects the distance that the user covers while traversing the path of the route. It isn’t a straight line distance between the [`origin`](../directionsrequest/origin.md) and [`destination`](../directionsrequest/destination.md).

## See Also

### Route details
- [steps](./steps.md)
  An array of steps that compose the overall route.
- [name](./name.md)
  The name assigned to the route.
- [expectedTravelTime](./expectedtraveltime.md)
  The expected travel time, in seconds.
- [transportType](./transporttype.md)
  The overall route transport type.
- [hasTolls](./hastolls.md)
  A Boolean value that indicates whether a route has tolls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/route/distance)*