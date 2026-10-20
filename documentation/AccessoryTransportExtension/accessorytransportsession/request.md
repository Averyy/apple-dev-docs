# AccessoryTransportSession.Request

**Framework**: Accessory Transport Extension  
**Kind**: class  
**Role**: Class

An incoming session request that your extension accepts or rejects.

**Availability**:
- iOS 26.2+

## Declaration

```swift
final class Request
```

## Topics

### Accepting and rejecting session requests
- [func accept<Handler>(() -> Handler) -> AccessoryTransportSession.Request.Decision](./request/accept%28_%29.md)
  Accepts the session request and provides an event handler.
- [func reject(error: AccessoryTransportSession.Error?) -> AccessoryTransportSession.Request.Decision](./request/reject%28error%29.md)
  Rejects the session request.
- [AccessoryTransportSession.Request.Decision](./request/decision.md)
  An opaque type returned from the incoming session handler of an event listener.
### Inspecting request properties
- [let session: AccessoryTransportSession](./request/session.md)
  The session to which the request belongs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/request)*