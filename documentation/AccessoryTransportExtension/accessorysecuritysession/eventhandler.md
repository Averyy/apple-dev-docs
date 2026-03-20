# AccessorySecuritySession.EventHandler

**Framework**: Accessory Transport Extension  
**Kind**: protocol

A protocol that defines methods for handling security session events.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
protocol EventHandler
```

#### Overview

Implement this protocol to respond to key exchange events and session invalidation.

## Topics

### Handling security events
- [func securityEventHandler(event: AccessorySecurity.Event)](accessorysecuritysession/eventhandler/securityeventhandler(event:).md)
  Handles security events that occur during the key exchange process.
### Handling the session life cycle
- [func invalidationHandler(error: (any Error)?)](accessorysecuritysession/eventhandler/invalidationhandler(error:).md)
  Handles session invalidation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession/eventhandler)*