# steps

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

An array of steps that compose the overall route.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
steps: RouteStep[];
```

#### Discussion

The array contains one or more [`RouteStep`](../routestep.md) objects representing distinct portions of the route. Each step corresponds to a single direction to follow along the route.

## See Also

### Route details
- [name](./name.md)
  The name assigned to the route.
- [distance](./distance.md)
  The route distance, in meters.
- [expectedTravelTime](./expectedtraveltime.md)
  The expected travel time, in seconds.
- [transportType](./transporttype.md)
  The overall route transport type.
- [hasTolls](./hastolls.md)
  A Boolean value that indicates whether a route has tolls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/route/steps)*