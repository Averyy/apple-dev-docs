# AccessoryMessage

**Framework**: Accessory Transport Extension  
**Kind**: struct

A structure that represents a message to send to an accessory.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
struct AccessoryMessage
```

#### Overview

Create accessory messages in your app’s [`AccessoryDataProvider`](accessorydataprovider.md) extension and send them using `AccessoryFeatureSession/sendMessage(_:)`. The system encrypts the message before delivering it to the transport extension.

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
### Enumerations
- [AccessoryMessage.Error](accessorymessage/error.md)
- [AccessoryMessage.Result](accessorymessage/result.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage)*