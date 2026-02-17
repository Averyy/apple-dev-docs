# CPMapTemplateWaypoint

**Framework**: CarPlay  
**Kind**: class

CPMapTemplateWaypoint represents a waypoint with associated travel estimates

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
class CPMapTemplateWaypoint
```

## Topics

### Initializers
- [init(waypoint: CPNavigationWaypoint, travelEstimates: CPTravelEstimates)](cpmaptemplatewaypoint/init(waypoint:travelestimates:).md)
  Initializes a new CPMapTemplateWaypoint with the specified waypoint and travel estimates.
### Instance Properties
- [var travelEstimates: CPTravelEstimates](cpmaptemplatewaypoint/travelestimates.md)
  Travel estimates for reaching this waypoint, including time and distance calculations.
- [var waypoint: CPNavigationWaypoint](cpmaptemplatewaypoint/waypoint.md)
  The navigation waypoint containing location-based information and guidance for a point of interest along a route.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatewaypoint)*