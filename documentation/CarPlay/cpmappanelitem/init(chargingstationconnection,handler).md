# init(chargingStationConnection:handler:)

**Framework**: CarPlay  
**Kind**: init

Creates a map panel item with charging connection details.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
init(chargingStationConnection: CPChargingStationConnection, handler: ((CPMapPanelItem, @escaping () -> Void) -> Void)? = nil)
```

#### Return Value

A map panel item initialized with charging information.

#### Discussion

For this type of item, the map panel displays the charging connector type and the supported power and voltage outputs.

## Parameters

- `chargingStationConnection`: The details of a charging station.
- `handler`: A closure you use to respond when someone taps or selects the item. The closure takes the map panel item as a parameter and returns no value. Specify `nil` if you don’t want to respond to interactions with the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelitem/init(chargingstationconnection:handler:))*