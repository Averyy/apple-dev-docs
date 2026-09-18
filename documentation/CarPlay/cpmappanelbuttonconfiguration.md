# CPMapPanelButtonConfiguration

**Framework**: CarPlay  
**Kind**: class

A type that manages the action buttons and travel estimates in a map panel.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class CPMapPanelButtonConfiguration
```

#### Overview

A `CPMapPanelbuttonConfiguration` object specifies the controls and details to display at the bottom of a [`CPMapPanel`](cpmappanel.md). Create this type when to add a primary action button and an optional secondary action button to the bottom of the panel. These buttons are separate from your map panel’s section content and remain pinned to the bottom of the panel during scrolling. You can also use this type to specify travel estimates you want to keep pinned to the bottom of the panel.

Instantiate this type and specify it with the rest of the panel content when initializing your [`CPMapPanel`](cpmappanel.md) object. You can’t change the button configuration details after you create your map panel.

## Topics

### Initializers
- [init(primaryAction: CPTextButton, secondaryButton: CPButton?, travelEstimates: CPTravelEstimates)](cpmappanelbuttonconfiguration/init(primaryaction:secondarybutton:travelestimates:).md)
  Initializes the map panel button configuration with the specified action buttons and travel estimates.
### Instance Properties
- [var secondaryButton: CPButton?](cpmappanelbuttonconfiguration/secondarybutton.md)
  The optional button you use to perform a secondary action.
- [var travelEstimates: CPTravelEstimates?](cpmappanelbuttonconfiguration/travelestimates.md)
  The travel estimates to display alongside the action buttons.

## Relationships

### Inherits From
- [CPPanelButtonConfiguration](cppanelbuttonconfiguration.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelbuttonconfiguration)*