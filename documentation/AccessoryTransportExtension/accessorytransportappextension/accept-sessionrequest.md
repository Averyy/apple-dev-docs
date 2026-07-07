# accept(sessionRequest:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Required**: Yes

Handles a new session request for the accessory.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
func accept(sessionRequest: AccessoryTransportSession.Request) -> AccessoryTransportSession.Request.Decision
```

#### Discussion

Implement this callback and respond to its invocations by the framework.

## Parameters

- `sessionRequest`: An [`AccessoryTransportSession.Request`](accessorytransportsession/request.md) instance you use to accept or reject the session.

## See Also

- [AccessoryTransportSession.Request.Decision](accessorytransportsession/request/decision.md)
  An opaque type returned from the incoming session handler of an event listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportappextension/accept(sessionrequest:))*