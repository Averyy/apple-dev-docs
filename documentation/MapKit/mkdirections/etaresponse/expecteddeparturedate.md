# expectedDepartureDate

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The expected departure time.

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
var expectedDepartureDate: Date { get }
```

```objc
@property (nonatomic, readonly) NSDate * expectedDepartureDate;
```

#### Discussion

The value of this property is dependent on whether you specify a departure date or arrival date in your [`MKDirections.Request`](../request.md) object. If you specify a departure date, the framework copies that date to this property. If you specify an arrival date, but not a departure date, the framework computes the departure date by subtracting the expected travel time from your arrival date. If you don’t specify an arrival date or departure date, the framework sets this property to the current time.

## See Also

### Getting the travel information
- [var expectedTravelTime: TimeInterval](./expectedtraveltime.md)
  The expected travel time, in seconds.
- [var expectedArrivalDate: Date](./expectedarrivaldate.md)
  The expected arrival time.
- [var distance: CLLocationDistance](./distance.md)
  The expected travel distance, in meters.
- [var transportType: MKDirectionsTransportType](./transporttype.md)
  The type of conveyance to use for determining the travel time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/etaresponse/expecteddeparturedate)*