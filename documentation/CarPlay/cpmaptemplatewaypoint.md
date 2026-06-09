# CPMapTemplateWaypoint

**Framework**: CarPlay  
**Kind**: class

CPMapTemplateWaypoint represents a waypoint with associated travel estimates

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
class CPMapTemplateWaypoint
```

## Topics

### Initializers
- [init?(coder: NSCoder)](cpmaptemplatewaypoint/init(coder:).md)
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
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatewaypoint)*