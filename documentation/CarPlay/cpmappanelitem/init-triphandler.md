# init(trip:handler:)

**Framework**: CarPlay  
**Kind**: init

Creates a map panel item with trip-related details.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
init(trip: CPTrip, handler: ((CPMapPanelItem, @escaping () -> Void) -> Void)? = nil)
```

#### Return Value

A map panel item initialized with trip information.

#### Discussion

For this type of item, the map panel shows journey’s destination point, its origin point, and the number of available route choices. This item type doesn’t show details about the individual route choice.

## Parameters

- `trip`: The trip object that contains the origin, destination, and route information.
- `handler`: A closure you use to respond when someone taps or selects the item. The closure takes the map panel item as a parameter and returns no value. Specify `nil` if you don’t want to respond to interactions with the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelitem/init(trip:handler:))*