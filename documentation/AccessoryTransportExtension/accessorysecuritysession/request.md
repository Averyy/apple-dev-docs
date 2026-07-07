# AccessorySecuritySession.Request

**Framework**: Accessory Transport Extension  
**Kind**: class

A structure that represents an incoming security session request.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
final class Request
```

#### Overview

The [`AccessoryTransportSecurity`](accessorytransportsecurity.md) protocol’s [`accept(sessionRequest:)`](accessorytransportsecurity/accept(sessionrequest:).md) method receives requests of this type.

## Topics

### Responding to the request
- [func accept<Handler>(() -> Handler) -> AccessorySecuritySession.Request.Decision](accessorysecuritysession/request/accept(_:).md)
  Accepts the session request with an event handler.
- [func reject(error: AccessorySecuritySession.Error?) -> AccessorySecuritySession.Request.Decision](accessorysecuritysession/request/reject(error:).md)
  Rejects the session request with an optional error.
- [AccessorySecuritySession.Request.Decision](accessorysecuritysession/request/decision.md)
  A structure that represents the decision to accept or reject a session request.
### Accessing the session
- [let session: AccessorySecuritySession](accessorysecuritysession/request/session.md)
  A security session object for the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession/request)*