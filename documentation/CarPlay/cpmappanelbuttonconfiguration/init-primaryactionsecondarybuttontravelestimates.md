# init(primaryAction:secondaryButton:travelEstimates:)

**Framework**: CarPlay  
**Kind**: init

Initializes the map panel button configuration with the specified action buttons and travel estimates.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
init(primaryAction: CPTextButton, secondaryButton: CPButton?, travelEstimates: CPTravelEstimates)
```

#### Return Value

A new map panel button configuration object.

## Parameters

- `primaryAction`: The text button for the primary action.
- `secondaryButton`: An optional button you can use to handle a secondary action. The configuration object stores a copy of the provided button in the [`secondaryButton`](cpmappanelbuttonconfiguration/secondarybutton.md) property.
- `travelEstimates`: The travel estimates to display with the buttons. The configuration object stores a copy of the provided travel estimates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelbuttonconfiguration/init(primaryaction:secondarybutton:travelestimates:))*