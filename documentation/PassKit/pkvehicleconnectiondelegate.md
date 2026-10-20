# PKVehicleConnectionDelegate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS
- visionOS 1.0+
- watchOS 8.5+

## Declaration

```swift
protocol PKVehicleConnectionDelegate : NSObjectProtocol
```

```objc
@protocol PKVehicleConnectionDelegate <NSObject>
```

## Topics

### Instance Methods
- [func sessionDidChange(PKVehicleConnectionSessionConnectionState)](./pkvehicleconnectiondelegate/sessiondidchange%28_%29.md)
- [func sessionDidReceive(Data)](./pkvehicleconnectiondelegate/sessiondidreceive%28_%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Digital car keys
- [class PKAddCarKeyPassConfiguration](./pkaddcarkeypassconfiguration.md)
  A specialized configuration object that PassKit uses when it creates a digital car key.
- [class PKVehicleConnectionSession](./pkvehicleconnectionsession.md)
- [enum PKVehicleConnectionSessionConnectionState](./pkvehicleconnectionsessionconnectionstate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkvehicleconnectiondelegate)*