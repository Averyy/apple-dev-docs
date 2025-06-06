# expectedTravelTime

**Framework**: MapKit  
**Kind**: property

The expected travel time, in seconds.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var expectedTravelTime: TimeInterval { get }
```

#### Discussion

The expected travel time reflects the time it takes to traverse the route, taking expected traffic into account. The actual amount of time may vary based on changes in traffic and other travel conditions.

## See Also

- [var expectedDepartureDate: Date](mkdirections/etaresponse/expecteddeparturedate.md)
  The expected departure time.
- [var expectedArrivalDate: Date](mkdirections/etaresponse/expectedarrivaldate.md)
  The expected arrival time.
- [var distance: CLLocationDistance](mkdirections/etaresponse/distance.md)
  The expected travel distance, in meters.
- [var transportType: MKDirectionsTransportType](mkdirections/etaresponse/transporttype.md)
  The type of conveyance to use for determining the travel time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/etaresponse/expectedtraveltime)*