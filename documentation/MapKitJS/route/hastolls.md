# hasTolls

**Framework**: MapKit JS  
**Kind**: property

A Boolean value that indicates whether a route has tolls.

**Availability**:
- MapKit JS 5.72+

## Declaration

```swift
attribute boolean? hasTolls;
```

#### Discussion

When `true`, this route has tolls. If `false`, this route doesn’t have any tolls. If undefined, the route may or may not have tolls.

## See Also

- [steps](route/steps.md)
  An array of steps that compose the overall route.
- [name](route/name.md)
  The name assigned to the route.
- [distance](route/distance.md)
  The route distance, in meters.
- [expectedTravelTime](route/expectedtraveltime.md)
  The expected travel time, in seconds.
- [transportType](route/transporttype.md)
  The overall route transport type.
- [mapkit.Directions.Transport](mapkit.directions.transport.md)
  The modes of transportation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/route/hastolls)*