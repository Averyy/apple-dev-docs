# accept(_:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Instance Method

Accepts the session request and provides an event handler.

**Availability**:
- iOS 26.2+

## Declaration

```swift
final func accept<Handler>(_ sessionRequestHandler: () -> Handler) -> AccessoryTransportSession.Request.Decision where Handler : AccessoryTransportSession.EventHandler
```

## Parameters

- `sessionRequestHandler`: A closure that produces an [`AccessoryTransportSession.EventHandler`](../eventhandler.md) to handle session events.

## See Also

### Accepting and rejecting session requests
- [func reject(error: AccessoryTransportSession.Error?) -> AccessoryTransportSession.Request.Decision](./reject%28error%29.md)
  Rejects the session request.
- [AccessoryTransportSession.Request.Decision](./decision.md)
  An opaque type returned from the incoming session handler of an event listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/request/accept(_:))*