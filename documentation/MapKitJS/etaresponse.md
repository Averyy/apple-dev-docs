# EtaResponse

**Framework**: MapKit JS  
**Kind**: struct

The estimated arrival times for a set of destinations.

**Availability**:
- MapKit JS 5.46+

## Declaration

```swift
dictionary EtaResponse {
	Object request;
	mapkit.Coordinate origin;
	EtaResult[] etas;
};
```

## Topics

### Estimated Arrival Time Responses
- [request](etaresponse/request.md)
  The request object associated with the estimated time of arrival response.
- [origin](etaresponse/origin.md)
  The coordinates that represent the starting point for estimated arrival time requests.
- [etas](etaresponse/etas.md)
  An array of estimated arrival times.

## See Also

- [eta](mapkit.directions/eta.md)
  Retrieves estimated arrival times to up to 10 destinations from a single starting point.
- [EtaRequestOptions](etarequestoptions.md)
  The options you may provide for requesting estimated arrival times.
- [EtaResult](etaresult.md)
  The mode of transportation, distance, and travel time estimates for a single destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/etaresponse)*