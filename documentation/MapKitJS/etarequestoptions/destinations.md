# destinations

**Framework**: MapKit JS  
**Kind**: property

An array of coordinates that represent end points for estimated arrival time requests.

**Availability**:
- MapKit JS 5.46+

## Declaration

```swift
destinations: CoordinateData[];
```

#### Discussion

A [`Coordinate`](coordinate.md) represents each destination in the array. You may get coordinates from [`search()`](search/search.md) or [`lookup()`](geocoder/lookup.md), which return [`Place`](place.md) objects that contain coordinates. You may provide up to 10 destinations in the array.

## See Also

- [origin](etarequestoptions/origin.md)
  The starting point for estimated arrival time requests.
- [departureDate](etarequestoptions/departuredate.md)
  The time of departure used in an estimated arrival time request.
- [transportType](etarequestoptions/transporttype.md)
  The mode of transportation the server uses when estimating arrival times.
- [signal](etarequestoptions/signal.md)
  A signal object allowing you to cancel the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/etarequestoptions/destinations)*