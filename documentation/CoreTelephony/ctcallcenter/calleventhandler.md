# callEventHandler

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

A closure dispatched when a call changes state.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: To monitor state changes in calls, use [`CXCallObserver`](../../CallKit/cxcallobserver.md) in [CallKit](../../CallKit/CallKit.md) instead.

## Declaration

```swift
var callEventHandler: ((CTCall) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^)(CTCall *) callEventHandler;
```

## See Also

### Responding to Cellular Call Events
- [var currentCalls: Set<CTCall>?](./currentcalls.md)
  An array representing the cellular calls in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcallcenter/calleventhandler)*