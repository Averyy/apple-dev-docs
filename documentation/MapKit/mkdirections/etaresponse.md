# MKDirections.ETAResponse

**Framework**: MapKit  
**Kind**: class

The travel-time information that Apple servers return.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
class ETAResponse
```

#### Overview

You don’t create instances of this class directly. Instead, you initiate a request for the travel time by calling the [`calculateETA(completionHandler:)`](mkdirections/calculateeta(completionhandler:).md) method of an [`MKDirections`](mkdirections.md) object. The completion handler you pass to that method receives an `MKDirections.ETAResponse` object with the results.

## Topics

### Getting the end points
- [var source: MKMapItem](mkdirections/etaresponse/source.md)
  The start point of the route.
- [var destination: MKMapItem](mkdirections/etaresponse/destination.md)
  The end point of the route.
### Getting the travel information
- [var expectedTravelTime: TimeInterval](mkdirections/etaresponse/expectedtraveltime.md)
  The expected travel time, in seconds.
- [var expectedDepartureDate: Date](mkdirections/etaresponse/expecteddeparturedate.md)
  The expected departure time.
- [var expectedArrivalDate: Date](mkdirections/etaresponse/expectedarrivaldate.md)
  The expected arrival time.
- [var distance: CLLocationDistance](mkdirections/etaresponse/distance.md)
  The expected travel distance, in meters.
- [var transportType: MKDirectionsTransportType](mkdirections/etaresponse/transporttype.md)
  The type of conveyance to use for determining the travel time.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MKDirections](mkdirections.md)
  A utility object that computes directions and travel-time information based on the route information you provide.
- [MKDirections.Request](mkdirections/request.md)
  The start and end points of a route, along with the planned mode of transportation.
- [MKDirections.Response](mkdirections/response.md)
  The route information that Apple servers return in response to your request for directions.
- [class MKRoute](mkroute.md)
  A single route between a requested start and end point.
- [MKRoute.Step](mkroute/step.md)
  One portion of an overall route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/etaresponse)*