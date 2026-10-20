# CTCallStateDisconnected

**Framework**: Core Telephony  
**Kind**: var  
**Role**: Global Variable

The call state upon call termination.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Obsolete and will be a useless stub before final removal. Replaced by <CallKit/CXCall.h> properties

## Declaration

```swift
let CTCallStateDisconnected: String
```

```c
extern NSString * const CTCallStateDisconnected;
```

## See Also

### Constants
- [let CTCallStateDialing: String](./ctcallstatedialing.md)
  The call state, before establishing the connection, when the user initiates the call.
- [let CTCallStateIncoming: String](./ctcallstateincoming.md)
  The call state, before establishing the connection, when a call is incoming but not yet answered by the user.
- [let CTCallStateConnected: String](./ctcallstateconnected.md)
  The call state when fully establishing the call for all parties involved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcallstatedisconnected)*