# transportType

**Framework**: MapKit JS  
**Kind**: property

The mode of transportation the server uses when estimating arrival times.

**Availability**:
- MapKit JS 5.46+

## Declaration

```swift
transportType?: TransportType;
```

#### Discussion

Use `transportType` to specify the mode of transportation for your [`route(request, callback)`](directions/route.md) and [`eta(request, callback)`](directions/eta.md) requests.

The default value of this property is [`Automobile`](transporttype/automobile.md).

## See Also

- [origin](etarequestoptions/origin.md)
  The starting point for estimated arrival time requests.
- [departureDate](etarequestoptions/departuredate.md)
  The time of departure used in an estimated arrival time request.
- [destinations](etarequestoptions/destinations.md)
  An array of coordinates that represent end points for estimated arrival time requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/etarequestoptions/transporttype)*