# callID

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

A unique identifier for the cellular call.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Obsolete and will be a useless stub before final removal. Replaced by <CallKit/CXCall.h> properties

## Declaration

```swift
var callID: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * callID;
```

## Discussion

Use this value to differentiate multiple active cellular calls.

## See Also

### Obtaining Information About a Cellular Call
- [var callState: String](./callstate.md)
  The state of the cellular call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcall/callid)*