# distance

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The expected travel distance, in meters.

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
var distance: CLLocationDistance { get }
```

```objc
@property (nonatomic, readonly) CLLocationDistance distance;
```

## Discussion

This property contains the overall distance traversed by the route.

## See Also

### Getting the travel information
- [var expectedTravelTime: TimeInterval](./expectedtraveltime.md)
  The expected travel time, in seconds.
- [var expectedDepartureDate: Date](./expecteddeparturedate.md)
  The expected departure time.
- [var expectedArrivalDate: Date](./expectedarrivaldate.md)
  The expected arrival time.
- [var transportType: MKDirectionsTransportType](./transporttype.md)
  The type of conveyance to use for determining the travel time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/etaresponse/distance)*