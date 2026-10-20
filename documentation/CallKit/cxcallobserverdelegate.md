# CXCallObserverDelegate

**Framework**: CallKit  
**Kind**: protocol  
**Role**: Protocol

A collection of methods the system calls when a call changes state.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol CXCallObserverDelegate : NSObjectProtocol
```

```objc
@protocol CXCallObserverDelegate <NSObject>
```

## Topics

### Responding to Changes in Call State
- [func callObserver(CXCallObserver, callChanged: CXCall)](./cxcallobserverdelegate/callobserver%28_,callchanged%29.md)
  Called when a call is changed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Call information
- [class CXCall](./cxcall.md)
  A telephony call.
- [class CXCallObserver](./cxcallobserver.md)
  A programmatic interface for an object that manages a list of active calls and observes call changes.
- [class CXHandle](./cxhandle.md)
  A way to reach a call recipient, such as a phone number or email address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallobserverdelegate)*