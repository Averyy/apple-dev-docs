# init(mapTemplateWaypoint:image:handler:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a map panel item with waypoint information.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
init(mapTemplateWaypoint: CPMapTemplateWaypoint, image: UIImage?, handler: ((CPMapPanelItem, @escaping () -> Void) -> Void)? = nil)
```

```objc
- (instancetype) initWithMapTemplateWaypoint:(CPMapTemplateWaypoint *) mapTemplateWaypoint image:(UIImage *) image handler:(void (^)(CPMapPanelItem *item, dispatch_block_t completionBlock)) handler;
```

## Return Value

A map panel item initialized with waypoint details.

## Discussion

For this type of item, the map panel displays the waypoint name, address, and any available route details.

## Parameters

- `mapTemplateWaypoint`: The waypoint information.
- `image`: An image to display for the waypoint.
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
- [init(chargingStationConnection: CPChargingStationConnection, handler: ((CPMapPanelItem, () -> Void) -> Void)?)](./init%28chargingstationconnection,handler%29.md)
  Creates a map panel item with charging connection details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelitem/init(maptemplatewaypoint:image:handler:))*