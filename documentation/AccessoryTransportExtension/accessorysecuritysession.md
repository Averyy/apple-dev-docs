# AccessorySecuritySession

**Framework**: Accessory Transport Extension  
**Kind**: class

A class that manages a security session between the extension and the system.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
class AccessorySecuritySession
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

#### Overview

The security session handles a key exchange process (see `AccessorySecurity/Event`) that establishes encrypted communication with your accessory.

## Topics

### Managing session requests
- [AccessorySecuritySession.Request](accessorysecuritysession/request.md)
  A structure that represents an incoming security session request.
### Handling session events
- [AccessorySecuritySession.EventHandler](accessorysecuritysession/eventhandler.md)
  A protocol that defines methods for handling security session events.
- [AccessorySecuritySession.Error](accessorysecuritysession/error.md)
### Accessing session properties
- [var description: String](accessorysecuritysession/description.md)
  String representation.
### Managing the session life cycle
- [func sendSecurityMessage(SecurityMessage) throws(AccessorySecuritySession.Error)](accessorysecuritysession/sendsecuritymessage(_:).md)
  Sends a security message to the system.
- [func cancel(error: AccessorySecuritySession.Error?)](accessorysecuritysession/cancel(error:).md)
  Cancels the security session.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [protocol AccessoryFeature](accessoryfeature.md)
  A protocol that defines a capability for an accessory data provider extension.
- [struct AccessoryMessage](accessorymessage.md)
  A structure that represents a message to send to an accessory.
- [struct TransportMessage](transportmessage.md)
  A structure that represents a message for transmission between the system and an accessory.
- [struct SecurityMessage](securitymessage.md)
  A structure that carries key material for negotiating a secure channel between the system and an accessory.
- [enum AccessoryTransport](accessorytransport.md)
  Supported transport types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession)*