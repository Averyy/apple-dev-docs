# init(routeChoice:handler:)

**Framework**: CarPlay  
**Kind**: init

Creates a map panel item with one of the route choices available for a trip.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
init(routeChoice: CPRouteChoice, handler: ((CPMapPanelItem, @escaping () -> Void) -> Void)? = nil)
```

#### Return Value

A map panel item initialized with a route choice.

#### Discussion

For this type of item, the map panel displays the relevant route choice summaries.

## Parameters

- `routeChoice`: A route choice for an upcoming trip.
- `handler`: A closure you use to respond when someone taps or selects the item. The closure takes the map panel item as a parameter and returns no value. Specify `nil` if you don’t want to respond to interactions with the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelitem/init(routechoice:handler:))*