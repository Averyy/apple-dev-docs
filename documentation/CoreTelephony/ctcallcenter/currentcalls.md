# currentCalls

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

An array representing the cellular calls in progress.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: To get a list of active calls, use [`CXCallObserver`](../../CallKit/cxcallobserver.md) in [CallKit](../../CallKit/CallKit.md) instead.

## Declaration

```swift
var currentCalls: Set<CTCall>? { get }
```

```objc
@property (retain, readonly, nullable) NSSet<CTCall *> * currentCalls;
```

#### Discussion

An array containing a `CTCall` object for each cellular call in progress. If no calls are in progress, the value of this property is `nil`.

## See Also

### Responding to Cellular Call Events
- [var callEventHandler: ((CTCall) -> Void)?](./calleventhandler.md)
  A closure dispatched when a call changes state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcallcenter/currentcalls)*