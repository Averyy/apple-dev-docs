# PKVehicleConnectionSession

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS
- visionOS 1.0+
- watchOS 8.5+

## Declaration

```swift
class PKVehicleConnectionSession
```

```objc
@interface PKVehicleConnectionSession : NSObject
```

## Topics

### Instance Properties
- [var connectionStatus: PKVehicleConnectionSessionConnectionState](./pkvehicleconnectionsession/connectionstatus.md)
- [var delegate: (any PKVehicleConnectionDelegate)?](./pkvehicleconnectionsession/delegate.md)
### Instance Methods
- [func invalidate()](./pkvehicleconnectionsession/invalidate%28%29.md)
- [func send(Data) throws](./pkvehicleconnectionsession/send%28_%29.md)
### Type Methods
- [class func session(for: PKSecureElementPass, delegate: any PKVehicleConnectionDelegate, completion: (PKVehicleConnectionSession?, (any Error)?) -> Void)](./pkvehicleconnectionsession/session%28for,delegate,completion%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Digital car keys
- [class PKAddCarKeyPassConfiguration](./pkaddcarkeypassconfiguration.md)
  A specialized configuration object that PassKit uses when it creates a digital car key.
- [protocol PKVehicleConnectionDelegate](./pkvehicleconnectiondelegate.md)
- [enum PKVehicleConnectionSessionConnectionState](./pkvehicleconnectionsessionconnectionstate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkvehicleconnectionsession)*