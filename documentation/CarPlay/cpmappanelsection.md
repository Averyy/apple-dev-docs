# CPMapPanelSection

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A single section of a map panel that you fill with a title and one or more items.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class CPMapPanelSection
```

```objc
@interface CPMapPanelSection : NSObject
```

## Overview

The `CPMapPanelSection` class organizes a single section of content in a [`CPMapPanel`](./cpmappanel.md) interface. In a navigation app, you use map panels to display relevant information such as route options or the location of charging stations on top of your custom map. Section objects manage one or more related items you want to display. For example, you might use one section to display upcoming charging stations and a different section to display route choices.

Create a `CPMapPanelSection` object and configure it with the section title and a [`CPMapPanelItem`](./cpmappanelitem.md) object for each item you want to display. Add the section to your [`CPMapPanel`](./cpmappanel.md) object before showing the panel from your map template. If you modify a section after the panel is visible, the system updates the section’s contents in your CarPlay interface.

## Topics

### Creating a map panel section
- [init(title: String?, items: [CPMapPanelItem])](./cpmappanelsection/init%28title,items%29.md)
  Initializes the section with the specified title and items.
- [init?(coder: NSCoder)](./cpmappanelsection/init%28coder%29.md)
### Accessing the section’s content
- [var title: String?](./cpmappanelsection/title.md)
  The localized string to display for the section title.
- [var items: [CPMapPanelItem]](./cpmappanelsection/items.md)
  The items to display in the section.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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
- [class CPMapPanelItem](./cpmappanelitem.md)
  A type that manages the waypoint, route, trip, and other information you display in a map panel.
- [class CPMapPanelButtonConfiguration](./cpmappanelbuttonconfiguration.md)
  A type that manages the action buttons and travel estimates in a map panel.
- [class CPChargingStationConnection](./cpchargingstationconnection.md)
  Details about the equipment at an electric vehicle charging station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelsection)*