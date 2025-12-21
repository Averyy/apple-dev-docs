# EtaResult

**Framework**: MapKit JS  
**Kind**: struct

The mode of transportation, distance, and travel time estimates for a single destination.

**Availability**:
- MapKit JS 5.46+

## Declaration

```swift
interface EtaResult
```

## Topics

### Estimated Arrival Times
- [transportType](etaresult/transporttype.md)
  The mode of transportation used to estimate the arrival time.
- [destination](etaresult/destination.md)
  The coordinates that represent the endpoint for estimated arrival time requests.
- [distance](etaresult/distance.md)
  The route distance in meters.
- [expectedTravelTime](etaresult/expectedtraveltime.md)
  The estimated travel time in seconds, including delays due to traffic.
- [staticTravelTime](etaresult/statictraveltime.md)
  The estimated travel time in seconds, excluding delays for traffic.

## See Also

- [eta(request, callback)](directions/eta.md)
  Retrieves estimated arrival times to up to 10 destinations from a single starting point.
- [interface EtaRequestOptions](etarequestoptions.md)
  The options you may provide for requesting estimated arrival times.
- [interface EtaResponse](etaresponse.md)
  The estimated arrival times for a set of destinations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/etaresult)*