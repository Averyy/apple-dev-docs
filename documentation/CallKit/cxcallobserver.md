# CXCallObserver

**Framework**: CallKit  
**Kind**: class

A programmatic interface for an object that manages a list of active calls and observes call changes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CXCallObserver
```

#### Overview

You can retrieve a list of active calls on an [`CXCallObserver`](cxcallobserver.md) object using the [`calls`](cxcallobserver/calls.md) property. You can also provide an object conforming to the [`CXCallObserverDelegate`](cxcallobserverdelegate.md) protocol as the call observer delegate using the [`setDelegate(_:queue:)`](cxcallobserver/setdelegate(_:queue:).md) method to respond to any active call changes.

VoIP apps typically interact with the [`CXCallObserver`](cxcallobserver.md) object returned by the [`callObserver`](cxcallcontroller/callobserver.md) property of a [`CXCallController`](cxcallcontroller.md) instance. However, any app can create a new [`CXCallObserver`](cxcallobserver.md) object to be notified of any calls activity on the system.

## Topics

### Setting a Delegate
- [func setDelegate((any CXCallObserverDelegate)?, queue: dispatch_queue_t?)](cxcallobserver/setdelegate(_:queue:).md)
  Sets a call observer delegate, specifying an optional queue on which to execute delegate methods.
### Accessing Calls
- [var calls: [CXCall]](cxcallobserver/calls.md)
  Returns the active calls of the telephony provider.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CXCall](cxcall.md)
  A telephony call.
- [protocol CXCallObserverDelegate](cxcallobserverdelegate.md)
  A collection of methods the system calls when a call changes state.
- [class CXHandle](cxhandle.md)
  A way to reach a call recipient, such as a phone number or email address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallobserver)*