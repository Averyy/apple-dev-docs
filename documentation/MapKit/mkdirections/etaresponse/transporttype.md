# transportType

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The type of conveyance to use for determining the travel time.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var transportType: MKDirectionsTransportType { get }
```

```objc
@property (nonatomic, readonly) MKDirectionsTransportType transportType;
```

#### Discussion

You specify the desired transportation type in your [`MKDirections.Request`](../request.md) object. If you specified [`any`](../../mkdirectionstransporttype/any.md), this property contains the transportation type used to generate the estimated information.

## See Also

### Getting the travel information
- [var expectedTravelTime: TimeInterval](./expectedtraveltime.md)
  The expected travel time, in seconds.
- [var expectedDepartureDate: Date](./expecteddeparturedate.md)
  The expected departure time.
- [var expectedArrivalDate: Date](./expectedarrivaldate.md)
  The expected arrival time.
- [var distance: CLLocationDistance](./distance.md)
  The expected travel distance, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/etaresponse/transporttype)*