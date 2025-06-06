# MKDirections.Response

**Framework**: MapKit  
**Kind**: class

The route information that Apple servers return in response to your request for directions.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
class Response
```

#### Overview

You don’t create instances of this class directly. Instead, you initiate a request for directions by calling the [`calculate(completionHandler:)`](mkdirections/calculate(completionhandler:).md) method of an [`MKDirections`](mkdirections.md) object. The completion handler you pass to that method receives an `MKDirections.Response` object with the results.

## Topics

### Getting the end points
- [var source: MKMapItem](mkdirections/response/source.md)
  The start point of the route.
- [var destination: MKMapItem](mkdirections/response/destination.md)
  The end point of the route.
### Getting the route information
- [var routes: [MKRoute]](mkdirections/response/routes.md)
  An array of route objects representing the directions between the start and end points.

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
- [MKDirections.ETAResponse](mkdirections/etaresponse.md)
  The travel-time information that Apple servers return.
- [class MKRoute](mkroute.md)
  A single route between a requested start and end point.
- [MKRoute.Step](mkroute/step.md)
  One portion of an overall route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/response)*