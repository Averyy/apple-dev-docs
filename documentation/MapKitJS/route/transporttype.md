# transportType

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

The overall route transport type.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
transportType: TransportType | null;
```

#### Discussion

This property reflects the primary transport type used for the route. Individual steps of the route might use different transport types.

## See Also

### Route details
- [steps](./steps.md)
  An array of steps that compose the overall route.
- [name](./name.md)
  The name assigned to the route.
- [distance](./distance.md)
  The route distance, in meters.
- [expectedTravelTime](./expectedtraveltime.md)
  The expected travel time, in seconds.
- [hasTolls](./hastolls.md)
  A Boolean value that indicates whether a route has tolls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/route/transporttype)*