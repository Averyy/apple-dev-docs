# MKDirections.ETAResponse

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

The travel-time information that Apple servers return.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class ETAResponse
```

```objc
@interface MKETAResponse : NSObject
```

#### Overview

You don’t create instances of this class directly. Instead, you initiate a request for the travel time by calling the [`calculateETA(completionHandler:)`](./calculateeta%28completionhandler%29.md) method of an [`MKDirections`](../mkdirections.md) object. The completion handler you pass to that method receives an `MKDirections.ETAResponse` object with the results.

## Topics

### Getting the end points
- [var source: MKMapItem](./etaresponse/source.md)
  The start point of the route.
- [var destination: MKMapItem](./etaresponse/destination.md)
  The end point of the route.
### Getting the travel information
- [var expectedTravelTime: TimeInterval](./etaresponse/expectedtraveltime.md)
  The expected travel time, in seconds.
- [var expectedDepartureDate: Date](./etaresponse/expecteddeparturedate.md)
  The expected departure time.
- [var expectedArrivalDate: Date](./etaresponse/expectedarrivaldate.md)
  The expected arrival time.
- [var distance: CLLocationDistance](./etaresponse/distance.md)
  The expected travel distance, in meters.
- [var transportType: MKDirectionsTransportType](./etaresponse/transporttype.md)
  The type of conveyance to use for determining the travel time.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Directions
- [class MKDirections](../mkdirections.md)
  A utility object that computes directions and travel-time information based on the route information you provide.
- [MKDirections.Request](./request.md)
  The start and end points of a route, along with the planned mode of transportation.
- [MKDirections.Response](./response.md)
  The route information that Apple servers return in response to your request for directions.
- [class MKRoute](../mkroute.md)
  A single route between a requested start and end point.
- [MKRoute.Step](../mkroute/step.md)
  One portion of an overall route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/etaresponse)*