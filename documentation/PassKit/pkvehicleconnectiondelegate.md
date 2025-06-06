# PKVehicleConnectionDelegate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: protocol

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS ?+
- visionOS 1.0+
- watchOS 8.5+

## Declaration

```swift
protocol PKVehicleConnectionDelegate : NSObjectProtocol
```

## Topics

### Instance Methods
- [func sessionDidChange(PKVehicleConnectionSessionConnectionState)](pkvehicleconnectiondelegate/sessiondidchange(_:).md)
- [func sessionDidReceive(Data)](pkvehicleconnectiondelegate/sessiondidreceive(_:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PKAddCarKeyPassConfiguration](pkaddcarkeypassconfiguration.md)
  A specialized configuration object that PassKit uses when it creates a digital car key.
- [class PKVehicleConnectionSession](pkvehicleconnectionsession.md)
- [enum PKVehicleConnectionSessionConnectionState](pkvehicleconnectionsessionconnectionstate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkvehicleconnectiondelegate)*