# AccessoryMessage

**Framework**: Accessory Transport Extension  
**Kind**: struct

A structure that represents a message to send to an accessory.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)
- Mac Catalyst 26.5+ (Beta)

## Declaration

```swift
struct AccessoryMessage
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

#### Overview

Create accessory messages in your app’s [`AccessoryDataProvider`](accessorydataprovider.md) extension and send them using [`send(message:)`](https://developer.apple.com/documentation/AccessoryNotifications/NotificationsForwarding/AccessoryNotificationsSession/send(message:)). The system encrypts the message before delivering it to the transport extension.

## Topics

### Creating messages
- [init(() -> AccessoryMessage)](accessorymessage/init(_:).md)
  Initializes an accessory message using a result builder closure.
- [AccessoryMessage.Builder](accessorymessage/builder.md)
  A builder that constructs accessory messages declaratively.
### Accessing message content
- [let payloads: [AccessoryMessage.Payload]](accessorymessage/payloads.md)
  An array of payload objects that comprise the message.
- [AccessoryMessage.Payload](accessorymessage/payload.md)
  A structure that represents a single data payload within an accessory message.
### Assessing outcomes
- [AccessoryMessage.Error](accessorymessage/error.md)
  An enumeration of errors that can occur during message transmission.
- [AccessoryMessage.Result](accessorymessage/result.md)
  An enumeration of results for message transmission.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AccessoryFeature](accessoryfeature.md)
  A protocol that defines a capability for an accessory data provider extension.
- [class AccessorySecuritySession](accessorysecuritysession.md)
  A class that manages a security session between the extension and the system.
- [struct TransportMessage](transportmessage.md)
  A structure that represents a message for transmission between the system and an accessory.
- [struct SecurityMessage](securitymessage.md)
  A structure that carries key material for negotiating a secure channel between the system and an accessory.
- [enum AccessoryTransport](accessorytransport.md)
  Supported transport types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage)*