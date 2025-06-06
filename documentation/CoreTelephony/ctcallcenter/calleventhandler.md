# callEventHandler

**Framework**: Core Telephony  
**Kind**: property

A closure dispatched when a call changes state.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var callEventHandler: ((CTCall) -> Void)? { get set }
```

## See Also

- [var currentCalls: Set<CTCall>?](ctcallcenter/currentcalls.md)
  An array representing the cellular calls in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcallcenter/calleventhandler)*