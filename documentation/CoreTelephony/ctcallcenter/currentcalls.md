# currentCalls

**Framework**: Core Telephony  
**Kind**: property

An array representing the cellular calls in progress.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var currentCalls: Set<CTCall>? { get }
```

#### Discussion

An array containing a `CTCall` object for each cellular call in progress. If no calls are in progress, the value of this property is `nil`.

## See Also

- [var callEventHandler: ((CTCall) -> Void)?](ctcallcenter/calleventhandler.md)
  A closure dispatched when a call changes state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcallcenter/currentcalls)*