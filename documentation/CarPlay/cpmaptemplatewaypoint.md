# CPMapTemplateWaypoint

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

CPMapTemplateWaypoint represents a waypoint with associated travel estimates

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
class CPMapTemplateWaypoint
```

```objc
@interface CPMapTemplateWaypoint : NSObject
```

## Topics

### Creating a trip
- [init(waypoint: CPNavigationWaypoint, travelEstimates: CPTravelEstimates)](./cpmaptemplatewaypoint/init%28waypoint,travelestimates%29.md)
  Initializes a new CPMapTemplateWaypoint with the specified waypoint and travel estimates.
- [init?(coder: NSCoder)](./cpmaptemplatewaypoint/init%28coder%29.md)
### Getting the route information
- [var waypoint: CPNavigationWaypoint](./cpmaptemplatewaypoint/waypoint.md)
  The navigation waypoint containing location-based information and guidance for a point of interest along a route.
- [var travelEstimates: CPTravelEstimates](./cpmaptemplatewaypoint/travelestimates.md)
  Travel estimates for reaching this waypoint, including time and distance calculations.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Trip and waypoints
- [class CPTrip](./cptrip.md)
  An object that represents a journey between an origin and a destination.
- [class CPNavigationWaypoint](./cpnavigationwaypoint.md)
  CPNavigationWaypoint represents a point of interest along a route that provides location-based information and guidance.
- [class CPMultiStopCardConfiguration](./cpmultistopcardconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatewaypoint)*