# PKVehicleConnectionSession

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS ?+
- visionOS 1.0+
- watchOS 8.5+

## Declaration

```swift
class PKVehicleConnectionSession
```

## Topics

### Instance Properties
- [var connectionStatus: PKVehicleConnectionSessionConnectionState](pkvehicleconnectionsession/connectionstatus.md)
- [var delegate: (any PKVehicleConnectionDelegate)?](pkvehicleconnectionsession/delegate.md)
### Instance Methods
- [func invalidate()](pkvehicleconnectionsession/invalidate.md)
- [func send(Data) throws](pkvehicleconnectionsession/send(_:).md)
### Type Methods
- [class func session(for: PKSecureElementPass, delegate: any PKVehicleConnectionDelegate, completion: (PKVehicleConnectionSession?, (any Error)?) -> Void)](pkvehicleconnectionsession/session(for:delegate:completion:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PKAddCarKeyPassConfiguration](pkaddcarkeypassconfiguration.md)
  A specialized configuration object that PassKit uses when it creates a digital car key.
- [protocol PKVehicleConnectionDelegate](pkvehicleconnectiondelegate.md)
- [enum PKVehicleConnectionSessionConnectionState](pkvehicleconnectionsessionconnectionstate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkvehicleconnectionsession)*