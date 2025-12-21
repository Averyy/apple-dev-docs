# origin

**Framework**: MapKit JS  
**Kind**: property

The starting point for estimated arrival time requests.

**Availability**:
- MapKit JS 5.46+

## Declaration

```swift
origin: Coordinate;
```

#### Discussion

The [`origin`](etarequestoptions/origin.md) can be a [`Coordinate`](coordinate.md), a [`Place`](place.md) object, or a string that’s an address. Other services, such as Search and Geocoder, return [`Place`](place.md) objects.

## See Also

- [departureDate](etarequestoptions/departuredate.md)
  The time of departure used in an estimated arrival time request.
- [destinations](etarequestoptions/destinations.md)
  An array of coordinates that represent end points for estimated arrival time requests.
- [transportType](etarequestoptions/transporttype.md)
  The mode of transportation the server uses when estimating arrival times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/etarequestoptions/origin)*