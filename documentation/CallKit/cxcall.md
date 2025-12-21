# CXCall

**Framework**: CallKit  
**Kind**: class

A telephony call.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CXCall
```

#### Overview

You don’t instantiate [`CXCall`](cxcall.md) objects directly. Instead, [`CXCall`](cxcall.md) objects are created by the telephony provider when an incoming call is received or an outgoing call is initiated.

Each [`CXCall`](cxcall.md) object is uniquely identified by a [`uuid`](cxcall/uuid.md). You primarily interact with calls by passing their unique identifiers to CallKit APIs. For example, to place a call on hold, you create an instance of [`CXSetHeldCallAction`](cxsetheldcallaction.md) with [`init(call:onHold:)`](cxsetheldcallaction/init(call:onhold:).md) passing the [`uuid`](cxcall/uuid.md) of the call and [`true`](https://developer.apple.com/documentation/Swift/true), create a [`CXTransaction`](cxtransaction.md) object containing the action, and then pass the transaction to an instance of [`CXCallController`](cxcallcontroller.md) using the [`request(_:completion:)`](cxcallcontroller/request(_:completion:).md) method.

You can use the [`CXCallObserver`](cxcallobserver.md) managed by a [`CXCallController`](cxcallcontroller.md) to access [`CXCall`](cxcall.md) instances for active calls using the [`calls`](cxcallobserver/calls.md) property, or provide an object conforming to the [`CXCallObserverDelegate`](cxcallobserverdelegate.md) protocol to be notified anytime a call is updated.

## Topics

### Accessing Call Attributes
- [var uuid: UUID](cxcall/uuid.md)
  The unique identifier for the call.
- [var isOutgoing: Bool](cxcall/isoutgoing.md)
  A Boolean value that indicates whether the call is outgoing.
- [var hasConnected: Bool](cxcall/hasconnected.md)
  A Boolean value that indicates whether the call has connected.
- [var hasEnded: Bool](cxcall/hasended.md)
  A Boolean value that indicates whether the call has ended.
- [var isOnHold: Bool](cxcall/isonhold.md)
  A Boolean value that indicates whether the call is on hold.

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

- [class CXCallObserver](cxcallobserver.md)
  A programmatic interface for an object that manages a list of active calls and observes call changes.
- [protocol CXCallObserverDelegate](cxcallobserverdelegate.md)
  A collection of methods the system calls when a call changes state.
- [class CXHandle](cxhandle.md)
  A way to reach a call recipient, such as a phone number or email address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcall)*