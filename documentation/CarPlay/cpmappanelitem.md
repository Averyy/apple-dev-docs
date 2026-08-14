# CPMapPanelItem

**Framework**: CarPlay  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class CPMapPanelItem
```

## Topics

### Initializers
- [init(chargingStationConnection: CPChargingStationConnection, handler: ((CPMapPanelItem, () -> Void) -> Void)?)](cpmappanelitem/init(chargingstationconnection:handler:).md)
  Initializes a map template item wrapping a @c CPChargingStationConnection.
- [init(mapTemplateWaypoint: CPMapTemplateWaypoint, image: UIImage?, handler: ((CPMapPanelItem, () -> Void) -> Void)?)](cpmappanelitem/init(maptemplatewaypoint:image:handler:).md)
  Initializes a map template item wrapping a @c CPMapTemplateWaypoint.
- [init(routeChoice: CPRouteChoice, handler: ((CPMapPanelItem, () -> Void) -> Void)?)](cpmappanelitem/init(routechoice:handler:).md)
  Initializes a map template item wrapping a @c CPRouteChoice.
- [init(routeDetails: [CPRouteDetail], handler: ((CPMapPanelItem, () -> Void) -> Void)?)](cpmappanelitem/init(routedetails:handler:).md)
  Initializes a map template item wrapping an array of @c CPRouteDetail objects.
- [init(travelEstimates: CPTravelEstimates, handler: ((CPMapPanelItem, () -> Void) -> Void)?)](cpmappanelitem/init(travelestimates:handler:).md)
  Initializes a map template item wrapping a @c CPTravelEstimates.
- [init(trip: CPTrip, handler: ((CPMapPanelItem, () -> Void) -> Void)?)](cpmappanelitem/init(trip:handler:).md)
  Initializes a map template item wrapping a @c CPTrip.

## Relationships

### Inherits From
- [CPPanelItem](cppanelitem.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelitem)*