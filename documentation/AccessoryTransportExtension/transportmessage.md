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

#### Overview

The [`AccessoryTransportSession.EventHandler`](accessorytransportsession/eventhandler.md) protocol’s [`messageReceived(_:completion:)`](accessorytransportsession/eventhandler/messagereceived(_:completion:).md) method receives messages of this type from the system. Use the [`sendMessageToDataProvider(_:)`](accessorytransportsession/sendmessagetodataprovider(_:).md) method to send messages from your accessory back to the data provider extension.

#### Correlate Messages with Capabilities

The [`sessionID`](transportmessage/sessionid.md) property identifies the capability session to which the message belongs. The system generates this identifier at feature enrollment time, and the value is fixed while the accessory remains paired through AccessorySetupKit.

## Topics

### Creating a transport message
- [init(sessionID: UUID, data: Data)](transportmessage/init(sessionid:data:).md)
  Initializes a transport message for a specific capability session.
### Accessing message content
- [let data: Data](transportmessage/data.md)
  A data object that contains the message content.
- [let sessionID: UUID](transportmessage/sessionid.md)
  A unique identifier for the message’s capability session.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol AccessoryFeature](accessoryfeature.md)
  A protocol that defines a capability for an accessory data provider extension.
- [struct AccessoryMessage](accessorymessage.md)
  A structure that represents a message to send to an accessory.
- [class AccessorySecuritySession](accessorysecuritysession.md)
  A class that manages a security session between the extension and the system.
- [struct SecurityMessage](securitymessage.md)
  A structure that carries key material for a secure channel between the system and an accessory.
- [enum AccessoryTransport](accessorytransport.md)
  Transport methods for communicating with an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/transportmessage)*