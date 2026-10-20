# CXCallObserver

**Framework**: CallKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface CXCallObserver : NSObject
```

#### Overview

You can retrieve a list of active calls on an [`CXCallObserver`](./cxcallobserver.md) object using the [`calls`](./cxcallobserver/calls.md) property. You can also provide an object conforming to the [`CXCallObserverDelegate`](./cxcallobserverdelegate.md) protocol as the call observer delegate using the [`setDelegate(_:queue:)`](./cxcallobserver/setdelegate%28_,queue%29.md) method to respond to any active call changes.

VoIP apps typically interact with the [`CXCallObserver`](./cxcallobserver.md) object returned by the [`callObserver`](./cxcallcontroller/callobserver.md) property of a [`CXCallController`](./cxcallcontroller.md) instance. However, any app can create a new [`CXCallObserver`](./cxcallobserver.md) object to be notified of any calls activity on the system.

## Topics

### Setting a Delegate
- [func setDelegate((any CXCallObserverDelegate)?, queue: dispatch_queue_t?)](./cxcallobserver/setdelegate%28_,queue%29.md)
  Sets a call observer delegate, specifying an optional queue on which to execute delegate methods.
### Accessing Calls
- [var calls: [CXCall]](./cxcallobserver/calls.md)
  Returns the active calls of the telephony provider.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Call information
- [class CXCall](./cxcall.md)
  A telephony call.
- [protocol CXCallObserverDelegate](./cxcallobserverdelegate.md)
  A collection of methods the system calls when a call changes state.
- [class CXHandle](./cxhandle.md)
  A way to reach a call recipient, such as a phone number or email address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallobserver)*