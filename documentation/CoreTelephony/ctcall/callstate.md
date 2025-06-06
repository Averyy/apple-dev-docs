# callState

**Framework**: Core Telephony  
**Kind**: property

The state of the cellular call.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var callState: String { get }
```

#### Discussion

A cellular call’s initial state is either [`CTCallStateDialing`](ctcallstatedialing.md) or [`CTCallStateIncoming`](ctcallstateincoming.md). After establishing the call for all parties involved, the state transitions to [`CTCallStateConnected`](ctcallstateconnected.md). When the call ends, the state transitions to [`CTCallStateDisconnected`](ctcallstatedisconnected.md).

## See Also

- [var callID: String](ctcall/callid.md)
  A unique identifier for the cellular call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcall/callstate)*