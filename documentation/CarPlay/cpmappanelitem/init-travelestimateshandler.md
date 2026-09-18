# init(travelEstimates:handler:)

**Framework**: CarPlay  
**Kind**: init

Creates a map panel item with travel estimate information.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
init(travelEstimates: CPTravelEstimates, handler: ((CPMapPanelItem, @escaping () -> Void) -> Void)? = nil)
```

#### Return Value

A map panel item initialized with travel estimates.

#### Discussion

For this type of item, the map panel displays the expected arrival time, along with the remaining distance and time information.

## Parameters

- `travelEstimates`: The object that provides the remaining distance and time values for a trip.
- `handler`: A closure you use to respond when someone taps or selects the item. The closure takes the map panel item as a parameter and returns no value. Specify `nil` if you don’t want to respond to interactions with the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelitem/init(travelestimates:handler:))*