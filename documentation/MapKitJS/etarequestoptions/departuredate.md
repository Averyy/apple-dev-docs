# departureDate

**Framework**: MapKit JS  
**Kind**: property

The time of departure used in an estimated arrival time request.

**Availability**:
- MapKit JS 5.46+

## Declaration

```swift
departureDate?: Date;
```

#### Discussion

If you don’t specify a departure date, the server will use the current date and time when you make the request.

## See Also

- [origin](etarequestoptions/origin.md)
  The starting point for estimated arrival time requests.
- [destinations](etarequestoptions/destinations.md)
  An array of coordinates that represent end points for estimated arrival time requests.
- [transportType](etarequestoptions/transporttype.md)
  The mode of transportation the server uses when estimating arrival times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/etarequestoptions/departuredate)*