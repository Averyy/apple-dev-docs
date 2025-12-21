# EtaRequestOptions

**Framework**: MapKit JS  
**Kind**: struct

The options you may provide for requesting estimated arrival times.

**Availability**:
- MapKit JS 5.46+

## Declaration

```swift
interface EtaRequestOptions
```

#### Overview

[`EtaRequestOptions`](etarequestoptions.md) accepts an array of destinations, but only accepts one `origin`, one `transportType`, and one `departureDate`. In other words, you can request the estimated arrival times from one place to 10 other places via one mode of transportation at one time.

## Topics

### ETA Request
- [origin](etarequestoptions/origin.md)
  The starting point for estimated arrival time requests.
- [departureDate](etarequestoptions/departuredate.md)
  The time of departure used in an estimated arrival time request.
- [destinations](etarequestoptions/destinations.md)
  An array of coordinates that represent end points for estimated arrival time requests.
- [transportType](etarequestoptions/transporttype.md)
  The mode of transportation the server uses when estimating arrival times.
### Instance Properties
- [arrivalDate](etarequestoptions/arrivaldate.md)
  The arrival date for the trip.

## See Also

- [eta(request, callback)](directions/eta.md)
  Retrieves estimated arrival times to up to 10 destinations from a single starting point.
- [interface EtaResponse](etaresponse.md)
  The estimated arrival times for a set of destinations.
- [interface EtaResult](etaresult.md)
  The mode of transportation, distance, and travel time estimates for a single destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/etarequestoptions)*