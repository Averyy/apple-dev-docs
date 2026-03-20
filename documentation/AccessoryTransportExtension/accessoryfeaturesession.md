# AccessoryFeatureSession

**Framework**: Accessory Transport Extension  
**Kind**: protocol

A protocol that manages a session for a specific feature capability.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
protocol AccessoryFeatureSession : Sendable
```

#### Overview

Implement this protocol to handle the life cycle of a feature session, including activation, message handling, and invalidation.

## Topics

### Managing the session life cycle
- [func invalidate()](accessoryfeaturesession/invalidate.md)
  Invalidates the feature session.
### Handling messages
- [func messageHandler(AccessoryMessage)](accessoryfeaturesession/messagehandler(_:).md)
  Handles incoming messages from the accessory.
- [func sendMessage(AccessoryMessage) async throws](accessoryfeaturesession/sendmessage(_:).md)
  Sends a message to the accessory through the system.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AccessoryFeature](accessoryfeature.md)
  A protocol that defines a capability for an accessory data provider extension.
- [struct AccessoryMessage](accessorymessage.md)
  A structure that represents a message to send to an accessory.
- [class AccessorySecuritySession](accessorysecuritysession.md)
  A class that manages a security session between the extension and the system.
- [struct AccessorySecurity](accessorysecurity.md)
  Types of security events and cryptography operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeaturesession)*