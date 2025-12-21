# AccessoryTransportSession.Request

**Framework**: AccessoryTransportExtension  
**Kind**: class

An incoming session request, which the extension can accept or reject.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
final class Request
```

## Topics

### Accepting and rejecting session requests
- [func accept<Handler>(() -> Handler) -> AccessoryTransportSession.Request.Decision](accessorytransportsession/request/accept(_:).md)
  Accepts the session request and provides an event handler.
- [func reject(error: AccessoryTransportSession.Error?) -> AccessoryTransportSession.Request.Decision](accessorytransportsession/request/reject(error:).md)
  Rejects the session request.
- [AccessoryTransportSession.Request.Decision](accessorytransportsession/request/decision.md)
  An opaque type returned from the incoming session handler of an event listener.
### Inspecting request properties
- [let session: AccessoryTransportSession](accessorytransportsession/request/session.md)
  The session to which the request belongs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/request)*