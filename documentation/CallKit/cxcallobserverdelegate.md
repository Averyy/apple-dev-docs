# CXCallObserverDelegate

**Framework**: CallKit  
**Kind**: protocol

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

## Topics

### Responding to Changes in Call State
- [func callObserver(CXCallObserver, callChanged: CXCall)](cxcallobserverdelegate/callobserver(_:callchanged:).md)
  Called when a call is changed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CXCall](cxcall.md)
  A telephony call.
- [class CXCallObserver](cxcallobserver.md)
  A programmatic interface for an object that manages a list of active calls and observes call changes.
- [class CXHandle](cxhandle.md)
  A way to reach a call recipient, such as a phone number or email address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallobserverdelegate)*