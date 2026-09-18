# init(mapTemplateWaypoint:image:handler:)

**Framework**: CarPlay  
**Kind**: init

Creates a map panel item with waypoint information.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
init(mapTemplateWaypoint: CPMapTemplateWaypoint, image: UIImage?, handler: ((CPMapPanelItem, @escaping () -> Void) -> Void)? = nil)
```

#### Return Value

A map panel item initialized with waypoint details.

#### Discussion

For this type of item, the map panel displays the waypoint name, address, and any available route details.

## Parameters

- `mapTemplateWaypoint`: The waypoint information.
- `image`: An image to display for the waypoint.
- `handler`: A closure you use to respond when someone taps or selects the item. The closure takes the map panel item as a parameter and returns no value. Specify `nil` if you don’t want to respond to interactions with the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelitem/init(maptemplatewaypoint:image:handler:))*