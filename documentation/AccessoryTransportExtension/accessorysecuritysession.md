# AccessorySecuritySession

**Framework**: Accessory Transport Extension  
**Kind**: class

A class that manages a security session between the extension and the system.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
class AccessorySecuritySession
```

#### Overview

The security session handles a key exchange process (see `AccessorySecurity/Event`) that establishes encrypted communication with your accessory.

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
- [func cancel(error: AccessorySecuritySession.Error?)](accessorysecuritysession/cancel(error:).md)
  Cancels the security session.
### Instance Methods
- [func sendSecurityMessage(SecurityMessage) throws(AccessorySecuritySession.Error)](accessorysecuritysession/sendsecuritymessage(_:).md)
  Send security message to the host process.
### Enumerations
- [AccessorySecuritySession.Error](accessorysecuritysession/error.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [protocol AccessoryFeature](accessoryfeature.md)
  A protocol that defines a capability for an accessory data provider extension.
- [struct AccessoryMessage](accessorymessage.md)
  A structure that represents a message to send to an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession)*