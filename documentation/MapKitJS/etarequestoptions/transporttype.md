# transportType

**Framework**: MapKit JS  
**Kind**: property

The mode of transportation the server uses when estimating arrival times.

**Availability**:
- MapKit JS 5.46+

## Declaration

```swift
attribute mapkit.Directions.Transport transportType;
```

#### Discussion

Use transportType to specify the mode of transportation for your [`route`](mapkit.directions/route.md) and [`eta`](mapkit.directions/eta.md) requests.

The default value of this property is [`Automobile`](mapkit.directions.transport/automobile.md).

## See Also

- [origin](etarequestoptions/origin.md)
  The starting point for estimated arrival time requests.
- [departureDate](etarequestoptions/departuredate.md)
  The time of departure used in an estimated arrival time request.
- [destinations](etarequestoptions/destinations.md)
  An array of coordinates that represent end points for estimated arrival time requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/etarequestoptions/transporttype)*