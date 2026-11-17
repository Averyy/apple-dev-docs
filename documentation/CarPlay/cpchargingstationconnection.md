# CPChargingStationConnection

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

Details about the equipment at an electric vehicle charging station.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class CPChargingStationConnection
```

```objc
@interface CPChargingStationConnection : NSObject
```

## Overview

A `CPChargingStationConnection` object stores information an electric vehicle owner needs to know about a nearby charging station. This type specifies the kind of charging connector the station supports and the available voltage and power levels. Navigation apps display this information in a scrolling panel on top of their map content.

Instantiate this type and specify it with the rest of the panel content when initializing your [`CPMapPanel`](./cpmappanel.md) object. This type doesn’t support direct interactions, but you can add buttons to your map panel to perform any required actions. If the charging station supports multiple charging configurations, you can create multiple instances of this type for display in your map panel.

> **Note**: When displaying charging station connection details, also display configurations the current vehicle supports, if known.

## Topics

### Creating a charging station connection
- [init(connector: CPChargingStationConnection.Connector, voltage: Measurement<UnitElectricPotentialDifference>, power: Measurement<UnitPower>)](./cpchargingstationconnection/init%28connector,voltage,power%29.md)
  Creates a charging station connection object with information about a specific charging configuration.
- [init?(coder: NSCoder)](./cpchargingstationconnection/init%28coder%29.md)
### Getting the connector information
- [var connector: CPChargingStationConnection.Connector](./cpchargingstationconnection/connector-swift.property.md)
  The type of connector the station provides for vehicles.
- [var voltage: Measurement<UnitElectricPotentialDifference>](./cpchargingstationconnection/voltage.md)
  The supported voltage level at the charging station.
- [var power: Measurement<UnitPower>](./cpchargingstationconnection/power.md)
  The supported power level at the charging station.
- [CPChargingStationConnection.Connector](./cpchargingstationconnection/connector-swift.enum.md)
  Constants for the connector types available at charging stations.

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
- [NSCopying](../Foundation/nscopying.md)
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
- [class CPMapPanelButtonConfiguration](./cpmappanelbuttonconfiguration.md)
  A type that manages the action buttons and travel estimates in a map panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpchargingstationconnection)*