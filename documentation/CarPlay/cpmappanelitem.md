# CPMapPanelItem

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A type that manages the waypoint, route, trip, and other information you display in a map panel.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class CPMapPanelItem
```

```objc
@interface CPMapPanelItem : CPPanelItem
```

#### Overview

A `CPMapPanelItem` object stores navigation-related information and manages interactions with that information. When creating a [`CPMapPanel`](./cpmappanel.md) to display over your custom map, configure it with one or more items with the information you want to display. Use items to display information about:

Trip details for a particular journey Travel estimates for a trip Route choices between a start and end point Route-related details such as costs and consumption metrics Charging station connection details Navigation waypoints

Create one or more `CPMapPanelItem` objects and add them to a [`CPMapPanelSection`](./cpmappanelsection.md). You can add multiple items to a section and each item can contain different information. For example, you might include one item with the trip details and additional items to present route-specific options. Provide a handler with your item if you want to respond when someone taps or selects the item.

Each type of item displays different information from the map panel interface. For example, an item you initialize with a [`CPTrip`](./cptrip.md) object displays the trip’s destination and origin plus the number of route choices. When configuring a section, you might include multiple items of different types to present a complete view of the trip.

## Topics

### Initializers
- [init(chargingStationConnection: CPChargingStationConnection, handler: ((CPMapPanelItem, () -> Void) -> Void)?)](./cpmappanelitem/init%28chargingstationconnection,handler%29.md)
  Creates a map panel item with charging connection details.
- [init(mapTemplateWaypoint: CPMapTemplateWaypoint, image: UIImage?, handler: ((CPMapPanelItem, () -> Void) -> Void)?)](./cpmappanelitem/init%28maptemplatewaypoint,image,handler%29.md)
  Creates a map panel item with waypoint information.
- [init(routeChoice: CPRouteChoice, handler: ((CPMapPanelItem, () -> Void) -> Void)?)](./cpmappanelitem/init%28routechoice,handler%29.md)
  Creates a map panel item with one of the route choices available for a trip.
- [init(routeDetails: [CPRouteDetail], handler: ((CPMapPanelItem, () -> Void) -> Void)?)](./cpmappanelitem/init%28routedetails,handler%29.md)
  Creates a map panel item with route details.
- [init(travelEstimates: CPTravelEstimates, handler: ((CPMapPanelItem, () -> Void) -> Void)?)](./cpmappanelitem/init%28travelestimates,handler%29.md)
  Creates a map panel item with travel estimate information.
- [init(trip: CPTrip, handler: ((CPMapPanelItem, () -> Void) -> Void)?)](./cpmappanelitem/init%28trip,handler%29.md)
  Creates a map panel item with trip-related details.

## Relationships

### Inherits From
- [CPPanelItem](./cppanelitem.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelitem)*