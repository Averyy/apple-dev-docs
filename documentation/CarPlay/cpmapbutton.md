# CPMapButton

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A button that represents an action that a map template displays on the CarPlay screen.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class CPMapButton
```

```objc
@interface CPMapButton : NSObject
```

## Topics

### Creating a map button
- [init(handler: ((CPMapButton) -> Void)?)](./cpmapbutton/init%28handler%29.md)
  Creates a new map button.
### Managing the images
- [var image: UIImage?](./cpmapbutton/image.md)
  The image to display on the button.
- [var focusedImage: UIImage?](./cpmapbutton/focusedimage.md)
  The image to display when focus is on the button.
### Configuring the button
- [var isEnabled: Bool](./cpmapbutton/isenabled.md)
  A Boolean value that enables and disables the map button.
- [var isHidden: Bool](./cpmapbutton/ishidden.md)
  A Boolean value that hides and shows the map button.
### Initializers
- [init?(coder: NSCoder)](./cpmapbutton/init%28coder%29.md)

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
- [Sendable](../Swift/sendable.md)

## See Also

### Maps
- [class CPMapTemplate](./cpmaptemplate.md)
  A template that displays a navigation overlay that your app draws on the map.
- [class CPMapPanel](./cpmappanel.md)
  An overlay for a custom map interface that shows navigation-related instructions or information over a portion of the map.
- [class CPMapPanelSection](./cpmappanelsection.md)
  A single section of a map panel that you fill with a title and one or more items.
- [class CPMapPanelItem](./cpmappanelitem.md)
  A type that manages the waypoint, route, trip, and other information you display in a map panel.
- [class CPMapPanelButtonConfiguration](./cpmappanelbuttonconfiguration.md)
  A type that manages the action buttons and travel estimates in a map panel.
- [class CPChargingStationConnection](./cpchargingstationconnection.md)
  Details about the equipment at an electric vehicle charging station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmapbutton)*