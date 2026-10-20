# reject(error:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Instance Method

Rejects the session request.

**Availability**:
- iOS 26.2+

## Declaration

```swift
final func reject(error: AccessoryTransportSession.Error?) -> AccessoryTransportSession.Request.Decision
```

## Parameters

- `error`: An error that indicates why the extension rejected the request.

## See Also

### Accepting and rejecting session requests
- [func accept<Handler>(() -> Handler) -> AccessoryTransportSession.Request.Decision](./accept%28_%29.md)
  Accepts the session request and provides an event handler.
- [AccessoryTransportSession.Request.Decision](./decision.md)
  An opaque type returned from the incoming session handler of an event listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/request/reject(error:))*