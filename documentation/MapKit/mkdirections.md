# MKDirections

**Framework**: MapKit  
**Kind**: class

A utility object that computes directions and travel-time information based on the route information you provide.

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
class MKDirections
```

## Mentions

- [Enabling Maps capability in Xcode](enabling-maps-capability-in-xcode.md)

#### Overview

You use an `MKDirections` object to ask the Apple servers to provide walking or driving directions for a route, which you specify using an [`MKDirections.Request`](mkdirections/request.md) object. After making a request, MapKit delivers the results asynchronously to the completion handler that you provide. You can also get the estimated travel time for the route.

Each `MKDirections` object handles a single request for directions, although you can cancel and restart that request as needed. You can create multiple instances of this class and process different route requests at the same time, but make requests only when you plan to present the corresponding route information to the user. Apps may receive an [`MKError.Code.loadingThrottled`](mkerror/code/loadingthrottled.md) error if the device makes too many requests in too short a time period.

## Topics

### Creating a directions object
- [init(request: MKDirections.Request)](mkdirections/init(request:).md)
  Creates and returns a directions object using the specified request.
- [MKDirections.Request](mkdirections/request.md)
  The start and end points of a route, along with the planned mode of transportation.
- [MKDirections.RoutePreference](mkdirections/routepreference.md)
  Options that modify how the framework selects routes when calculating directions.
### Getting the directions
- [func calculate(completionHandler: (MKDirections.Response?, (any Error)?) -> Void)](mkdirections/calculate(completionhandler:).md)
  Begins calculating the requested route information asynchronously.
- [MKDirections.DirectionsHandler](mkdirections/directionshandler.md)
  The block to use for processing the requested route information.
- [MKDirections.Response](mkdirections/response.md)
  The route information that Apple servers return in response to your request for directions.
### Getting the ETA
- [func calculateETA(completionHandler: (MKDirections.ETAResponse?, (any Error)?) -> Void)](mkdirections/calculateeta(completionhandler:).md)
  Begins calculating the requested travel-time information asynchronously.
- [MKDirections.ETAHandler](mkdirections/etahandler.md)
  The block to use for processing travel-time information.
- [MKDirections.ETAResponse](mkdirections/etaresponse.md)
  The travel-time information that Apple servers return.
### Managing the request
- [func cancel()](mkdirections/cancel.md)
  Cancels a pending request.
- [var isCalculating: Bool](mkdirections/iscalculating.md)
  A Boolean value that indicates whether a request is in process.

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

- [MKDirections.Request](mkdirections/request.md)
  The start and end points of a route, along with the planned mode of transportation.
- [MKDirections.Response](mkdirections/response.md)
  The route information that Apple servers return in response to your request for directions.
- [MKDirections.ETAResponse](mkdirections/etaresponse.md)
  The travel-time information that Apple servers return.
- [class MKRoute](mkroute.md)
  A single route between a requested start and end point.
- [MKRoute.Step](mkroute/step.md)
  One portion of an overall route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections)*