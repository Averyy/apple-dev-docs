# init(routeDetails:handler:)

**Framework**: CarPlay  
**Kind**: init

Creates a map panel item with route details.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
init(routeDetails: [CPRouteDetail], handler: ((CPMapPanelItem, @escaping () -> Void) -> Void)? = nil)
```

#### Return Value

A map panel item initialized with route details.

#### Discussion

For this type of item, the map panel displays up to four route details per item.

## Parameters

- `routeDetails`: The route detail that helps someone make an informed decision about their journey.
- `handler`: A closure you use to respond when someone taps or selects the item. The closure takes the map panel item as a parameter and returns no value. Specify `nil` if you don’t want to respond to interactions with the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelitem/init(routedetails:handler:))*