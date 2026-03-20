# AccessoryMessage

**Framework**: Accessory Transport Extension  
**Kind**: struct

A structure that represents a message to send to an accessory.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
struct AccessoryMessage
```

#### Overview

Create accessory messages in your app’s [`AccessoryDataProvider`](accessorydataprovider.md) extension and send them using [`sendMessage(_:)`](accessoryfeaturesession/sendmessage(_:).md). The system encrypts the message before delivering it to the transport extension.

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
### Specifying transport options
- [AccessoryMessage.Transport](accessorymessage/transport.md)
  Options for transporting message payloads.
- [AccessoryMessage.Size](accessorymessage/size.md)
  Options to specify sizes of accessory messages.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AccessoryFeature](accessoryfeature.md)
  A protocol that defines a capability for an accessory data provider extension.
- [protocol AccessoryFeatureSession](accessoryfeaturesession.md)
  A protocol that manages a session for a specific feature capability.
- [class AccessorySecuritySession](accessorysecuritysession.md)
  A class that manages a security session between the extension and the system.
- [struct AccessorySecurity](accessorysecurity.md)
  Types of security events and cryptography operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage)*