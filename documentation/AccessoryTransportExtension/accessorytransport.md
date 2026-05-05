# AccessoryTransport

**Framework**: Accessory Transport Extension  
**Kind**: enum

Supported transport types.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
enum AccessoryTransport
```

## Topics

### Enumeration Cases
- [AccessoryTransport.bluetooth](accessorytransport/bluetooth.md)
  A transport method that uses Bluetooth for data delivery.
- [AccessoryTransport.internet](accessorytransport/internet.md)
  A transport method that uses the internet for data delivery.
- [AccessoryTransport.localNetwork](accessorytransport/localnetwork.md)
  A transport method that uses the local network for data delivery.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AccessoryFeature](accessoryfeature.md)
  A protocol that defines a capability for an accessory data provider extension.
- [struct AccessoryMessage](accessorymessage.md)
  A structure that represents a message to send to an accessory.
- [class AccessorySecuritySession](accessorysecuritysession.md)
  A class that manages a security session between the extension and the system.
- [struct TransportMessage](transportmessage.md)
  A structure that represents a message for transmission between the system and an accessory.
- [struct SecurityMessage](securitymessage.md)
  A structure that carries key material for negotiating a secure channel between the system and an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransport)*