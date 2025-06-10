# MKRoute.Step

**Framework**: MapKit  
**Kind**: class

One portion of an overall route.

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
class Step
```

#### Overview

Each `MKRoute.Step` object corresponds to a single instruction that the person needs to follow when navigating between two points. For example, a step might involve following a single road until continuing along the route requires a turn.

You don’t create instances of this class directly. An [`MKRoute`](mkroute.md) object contains the `MKRoute.Step` objects associated with a route. For more information about requesting directions, see [`MKDirections`](mkdirections.md).

## Topics

### Getting the step geometry
- [var polyline: MKPolyline](mkroute/step/polyline.md)
  The detailed step geometry.
### Getting additional step details
- [var instructions: String](mkroute/step/instructions.md)
  The written instructions for following the path that the step represents.
- [var notice: String?](mkroute/step/notice.md)
  Additional notices that apply to the step.
- [var distance: CLLocationDistance](mkroute/step/distance.md)
  The step distance, in meters.
- [var transportType: MKDirectionsTransportType](mkroute/step/transporttype.md)
  The transport type of the step.

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
- [class MKRoute](mkroute.md)
  A single route between a requested start and end point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkroute/step)*