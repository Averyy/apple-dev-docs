# name

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

The name assigned to the route.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
name: string;
```

## Discussion

Display [`name`](./name.md) to the user so they can distinguish one route from another. MapKit JS localizes this string according to the [`Directions`](../directions.md) object’s [`language`](../directionsconstructoroptions/language.md) value.

## See Also

### Route details
- [steps](./steps.md)
  An array of steps that compose the overall route.
- [distance](./distance.md)
  The route distance, in meters.
- [expectedTravelTime](./expectedtraveltime.md)
  The expected travel time, in seconds.
- [transportType](./transporttype.md)
  The overall route transport type.
- [hasTolls](./hastolls.md)
  A Boolean value that indicates whether a route has tolls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/route/name)*