# init(primaryAction:secondaryButton:travelEstimates:)

**Framework**: CarPlay  
**Kind**: init

Initializes a map panel button configuration with a primary action, optional travel estimates, and an optional secondary button.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
init(primaryAction: CPTextButton, secondaryButton: CPButton?, travelEstimates: CPTravelEstimates)
```

#### Return Value

A new @c CPMapPanelButtonConfiguration instance.

## Parameters

- `primaryAction`: The primary text button for the panel.
- `secondaryButton`: An optional secondary button. Note: only the image property of this button is used. Any title provided will be dropped.
- `travelEstimates`: The travel estimates to display alongside the primary button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelbuttonconfiguration/init(primaryaction:secondarybutton:travelestimates:))*