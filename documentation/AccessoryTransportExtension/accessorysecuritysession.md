# AccessorySecuritySession

**Framework**: Accessory Transport Extension  
**Kind**: class

A class that manages a security session between the extension and the system.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
class AccessorySecuritySession
```

#### Overview

The security session handles a key exchange process (see [`AccessorySecurity.Event`](accessorysecurity/event.md)) that establishes encrypted communication with your accessory.

## Topics

### Managing session requests
- [AccessorySecuritySession.Request](accessorysecuritysession/request.md)
  A structure that represents an incoming security session request.
### Handling session events
- [AccessorySecuritySession.EventHandler](accessorysecuritysession/eventhandler.md)
  A protocol that defines methods for handling security session events.
### Accessing session properties
- [var description: String](accessorysecuritysession/description.md)
  A textual representation of the session.
### Managing the session life cycle
- [func cancel(error: (any Error)?)](accessorysecuritysession/cancel(error:).md)
  Cancels the security session.
- [func sendSecurityEvent(AccessorySecurity.Event) throws](accessorysecuritysession/sendsecurityevent(_:).md)
  Sends a security event to the system.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [protocol AccessoryFeature](accessoryfeature.md)
  A protocol that defines a capability for an accessory data provider extension.
- [protocol AccessoryFeatureSession](accessoryfeaturesession.md)
  A protocol that manages a session for a specific feature capability.
- [struct AccessoryMessage](accessorymessage.md)
  A structure that represents a message to send to an accessory.
- [struct AccessorySecurity](accessorysecurity.md)
  Types of security events and cryptography operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession)*