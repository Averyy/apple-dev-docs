# CPMapPanelButtonConfiguration

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A type that manages the action buttons and travel estimates in a map panel.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class CPMapPanelButtonConfiguration
```

```objc
@interface CPMapPanelButtonConfiguration : CPPanelButtonConfiguration
```

## Overview

A `CPMapPanelbuttonConfiguration` object specifies the controls and details to display at the bottom of a [`CPMapPanel`](./cpmappanel.md). Create this type when to add a primary action button and an optional secondary action button to the bottom of the panel. These buttons are separate from your map panel’s section content and remain pinned to the bottom of the panel during scrolling. You can also use this type to specify travel estimates you want to keep pinned to the bottom of the panel.

Instantiate this type and specify it with the rest of the panel content when initializing your [`CPMapPanel`](./cpmappanel.md) object. You can’t change the button configuration details after you create your map panel.

## Topics

### Creating a map panel button configuration
- [init(primaryAction: CPTextButton, secondaryButton: CPButton?, travelEstimates: CPTravelEstimates)](./cpmappanelbuttonconfiguration/init%28primaryaction,secondarybutton,travelestimates%29.md)
  Initializes the map panel button configuration with the specified action buttons and travel estimates.
### Accessing the configuration details
- [var secondaryButton: CPButton?](./cpmappanelbuttonconfiguration/secondarybutton.md)
  The optional button you use to perform a secondary action.
- [var travelEstimates: CPTravelEstimates?](./cpmappanelbuttonconfiguration/travelestimates.md)
  The travel estimates to display alongside the action buttons.

## Relationships

### Inherits From
- [CPPanelButtonConfiguration](./cppanelbuttonconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Maps
- [class CPMapTemplate](./cpmaptemplate.md)
  A template that displays a navigation overlay that your app draws on the map.
- [class CPMapButton](./cpmapbutton.md)
  A button that represents an action that a map template displays on the CarPlay screen.
- [class CPMapPanel](./cpmappanel.md)
  An overlay for a custom map interface that shows navigation-related instructions or information over a portion of the map.
- [class CPMapPanelSection](./cpmappanelsection.md)
  A single section of a map panel that you fill with a title and one or more items.
- [class CPMapPanelItem](./cpmappanelitem.md)
  A type that manages the waypoint, route, trip, and other information you display in a map panel.
- [class CPChargingStationConnection](./cpchargingstationconnection.md)
  Details about the equipment at an electric vehicle charging station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelbuttonconfiguration)*