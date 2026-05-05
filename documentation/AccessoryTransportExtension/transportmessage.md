# TransportMessage

**Framework**: Accessory Transport Extension  
**Kind**: struct

A structure that represents a message for transmission between the system and an accessory.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
struct TransportMessage
```

## Topics

### Initializing a transport message
- [init(sessionID: UUID, data: Data)](transportmessage/init(sessionid:data:).md)
  Create a new message for a session.
### Inspecting message details
- [let data: Data](transportmessage/data.md)
  A data object that contains the message content.
- [let sessionID: UUID](transportmessage/sessionid.md)
  A unique identifier for tracking messages within a specific session.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AccessoryFeature](accessoryfeature.md)
  A protocol that defines a capability for an accessory data provider extension.
- [struct AccessoryMessage](accessorymessage.md)
  A structure that represents a message to send to an accessory.
- [class AccessorySecuritySession](accessorysecuritysession.md)
  A class that manages a security session between the extension and the system.
- [struct SecurityMessage](securitymessage.md)
  A structure that carries key material for negotiating a secure channel between the system and an accessory.
- [enum AccessoryTransport](accessorytransport.md)
  Supported transport types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/transportmessage)*