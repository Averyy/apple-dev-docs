# accept(sessionRequest:)

**Framework**: AccessoryTransportExtension  
**Kind**: method  
**Required**: Yes

Handles a new session request for the accessory, in response to a call from the framework.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
func accept(sessionRequest: AccessoryTransportSession.Request) -> AccessoryTransportSession.Request.Decision
```

## Parameters

- `sessionRequest`: An   instance you use to accept or reject the session.

## See Also

- [AccessoryTransportSession.Request.Decision](accessorytransportsession/request/decision.md)
  An opaque type returned from the incoming session handler of an event listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportappextension/accept(sessionrequest:))*