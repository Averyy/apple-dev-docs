# CTCallStateIncoming

**Framework**: Core Telephony  
**Kind**: var  
**Role**: Global Variable

The call state, before establishing the connection, when a call is incoming but not yet answered by the user.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Obsolete and will be a useless stub before final removal. Replaced by <CallKit/CXCall.h> properties

## Declaration

```swift
let CTCallStateIncoming: String
```

```c
extern NSString * const CTCallStateIncoming;
```

## See Also

### Constants
- [let CTCallStateDialing: String](./ctcallstatedialing.md)
  The call state, before establishing the connection, when the user initiates the call.
- [let CTCallStateConnected: String](./ctcallstateconnected.md)
  The call state when fully establishing the call for all parties involved.
- [let CTCallStateDisconnected: String](./ctcallstatedisconnected.md)
  The call state upon call termination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcallstateincoming)*