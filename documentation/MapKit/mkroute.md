# MKRoute

**Framework**: MapKit  
**Kind**: class

A single route between a requested start and end point.

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
class MKRoute
```

#### Overview

An `MKRoute` object defines the geometry for the route — that is, it contains line segments associated with specific map coordinates. A route object may also include other information, such as the name of the route, its distance, and the expected travel time.

You don’t create instances of this class directly. When you use an [`MKDirections`](mkdirections.md) object to request directions from Apple, the returned [`MKDirections.Response`](mkdirections/response.md) object contains the possible routes.

## Topics

### Getting the route geometry
- [var polyline: MKPolyline](mkroute/polyline.md)
  The detailed route geometry.
- [var steps: [MKRoute.Step]](mkroute/steps.md)
  The array of steps that create the overall route.
- [MKRoute.Step](mkroute/step.md)
  One portion of an overall route.
### Getting additional route details
- [var name: String](mkroute/name.md)
  The assigned name for the route.
- [var hasHighways: Bool](mkroute/hashighways.md)
  A Boolean value that indicates whether the route contains highways.
- [var hasTolls: Bool](mkroute/hastolls.md)
  A Boolean value that indicates whether the route has tolls.
- [var advisoryNotices: [String]](mkroute/advisorynotices.md)
  An array of advisory notice strings for the route.
- [var distance: CLLocationDistance](mkroute/distance.md)
  The route distance, in meters.
- [var expectedTravelTime: TimeInterval](mkroute/expectedtraveltime.md)
  The expected travel time, in seconds.
- [var transportType: MKDirectionsTransportType](mkroute/transporttype.md)
  The overall route transport type.

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
- [MKDirections.ETAResponse](mkdirections/etaresponse.md)
  The travel-time information that Apple servers return.
- [MKRoute.Step](mkroute/step.md)
  One portion of an overall route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkroute)*