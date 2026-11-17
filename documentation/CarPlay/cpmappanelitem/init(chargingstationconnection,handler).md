# init(chargingStationConnection:handler:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a map panel item with charging connection details.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
init(chargingStationConnection: CPChargingStationConnection, handler: ((CPMapPanelItem, @escaping () -> Void) -> Void)? = nil)
```

```objc
- (instancetype) initWithChargingStationConnection:(CPChargingStationConnection *) chargingStationConnection handler:(void (^)(CPMapPanelItem *item, dispatch_block_t completionBlock)) handler;
```

## Return Value

A map panel item initialized with charging information.

## Discussion

For this type of item, the map panel displays the charging connector type and the supported power and voltage outputs.

## Parameters

- `chargingStationConnection`: The details of a charging station.
- `handler`: A closure you use to respond when someone taps or selects the item. The closure takes the map panel item as a parameter and returns no value. Specify `nil` if you don’t want to respond to interactions with the item.

## See Also

### Creating map panel items
- [init(trip: CPTrip, handler: ((CPMapPanelItem, () -> Void) -> Void)?)](./init%28trip,handler%29.md)
  Creates a map panel item with trip-related details.
- [init(travelEstimates: CPTravelEstimates, handler: ((CPMapPanelItem, () -> Void) -> Void)?)](./init%28travelestimates,handler%29.md)
  Creates a map panel item with travel estimate information.
- [init(routeChoice: CPRouteChoice, handler: ((CPMapPanelItem, () -> Void) -> Void)?)](./init%28routechoice,handler%29.md)
  Creates a map panel item with one of the route choices available for a trip.
- [init(routeDetails: [CPRouteDetail], handler: ((CPMapPanelItem, () -> Void) -> Void)?)](./init%28routedetails,handler%29.md)
  Creates a map panel item with route details.
- [init(mapTemplateWaypoint: CPMapTemplateWaypoint, image: UIImage?, handler: ((CPMapPanelItem, () -> Void) -> Void)?)](./init%28maptemplatewaypoint,image,handler%29.md)
  Creates a map panel item with waypoint information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelitem/init(chargingstationconnection:handler:))*