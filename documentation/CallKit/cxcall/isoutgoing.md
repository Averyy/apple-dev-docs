# isOutgoing

**Framework**: CallKit  
**Kind**: property

A Boolean value that indicates whether the call is outgoing.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var isOutgoing: Bool { get }
```

#### Discussion

An outgoing call is a call initiated by the user, as opposed to an incoming call which is received by the telephony provider.

## See Also

- [var uuid: UUID](cxcall/uuid.md)
  The unique identifier for the call.
- [var hasConnected: Bool](cxcall/hasconnected.md)
  A Boolean value that indicates whether the call has connected.
- [var hasEnded: Bool](cxcall/hasended.md)
  A Boolean value that indicates whether the call has ended.
- [var isOnHold: Bool](cxcall/isonhold.md)
  A Boolean value that indicates whether the call is on hold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcall/isoutgoing)*