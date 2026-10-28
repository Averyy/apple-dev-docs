# callState

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

The state of the cellular call.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Obsolete and will be a useless stub before final removal. Replaced by <CallKit/CXCall.h> properties

## Declaration

```swift
var callState: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * callState;
```

## Discussion

A cellular call’s initial state is either [`CTCallStateDialing`](../ctcallstatedialing.md) or [`CTCallStateIncoming`](../ctcallstateincoming.md). After establishing the call for all parties involved, the state transitions to [`CTCallStateConnected`](../ctcallstateconnected.md). When the call ends, the state transitions to [`CTCallStateDisconnected`](../ctcallstatedisconnected.md).

## See Also

### Obtaining Information About a Cellular Call
- [var callID: String](./callid.md)
  A unique identifier for the cellular call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcall/callstate)*