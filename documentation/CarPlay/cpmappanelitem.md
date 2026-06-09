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
- [init(gridButtons: [CPGridButton])](cpmappanelitem/init(gridbuttons:).md)
  Initializes a map template item wrapping an array of @c CPGridButton objects.
- [init(listItem: CPListItem)](cpmappanelitem/init(listitem:).md)
  Initializes a map template item wrapping a @c CPListItem.
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
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelitem)*