# MKRoute.Step

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface MKRouteStep : NSObject
```

## Overview

Each `MKRoute.Step` object corresponds to a single instruction that the person needs to follow when navigating between two points. For example, a step might involve following a single road until continuing along the route requires a turn.

You don’t create instances of this class directly. An [`MKRoute`](../mkroute.md) object contains the `MKRoute.Step` objects associated with a route. For more information about requesting directions, see [`MKDirections`](../mkdirections.md).

## Topics

### Getting the step geometry
- [var polyline: MKPolyline](./step/polyline.md)
  The detailed step geometry.
### Getting additional step details
- [var instructions: String](./step/instructions.md)
  The written instructions for following the path that the step represents.
- [var notice: String?](./step/notice.md)
  Additional notices that apply to the step.
- [var distance: CLLocationDistance](./step/distance.md)
  The step distance, in meters.
- [var transportType: MKDirectionsTransportType](./step/transporttype.md)
  The transport type of the step.

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
- [MKDirections.Request](../mkdirections/request.md)
  The start and end points of a route, along with the planned mode of transportation.
- [MKDirections.Response](../mkdirections/response.md)
  The route information that Apple servers return in response to your request for directions.
- [MKDirections.ETAResponse](../mkdirections/etaresponse.md)
  The travel-time information that Apple servers return.
- [class MKRoute](../mkroute.md)
  A single route between a requested start and end point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkroute/step)*