# CXAction

**Framework**: CallKit  
**Kind**: class

An abstract class that declares a programmatic interface for objects that represent a telephony action.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CXAction
```

#### Overview

Each instance of [`CXAction`](cxaction.md) is uniquely identified by a [`uuid`](cxaction/uuid.md), which is generated on initialization. An action also tracks whether it has been completed or not.

To perform one or more actions, you add them to a new [`CXTransaction`](cxtransaction.md) object and pass the transaction to an instance of [`CXCallController`](cxcallcontroller.md) using the [`request(_:completion:)`](cxcallcontroller/request(_:completion:).md) method. After each action is performed by the telephony provider, the provider’s delegate calls either the [`fulfill()`](cxaction/fulfill().md) method, indicating that the action was successfully performed, or the [`fail()`](cxaction/fail().md) method, to indicate that an error occurred; both of these methods set the [`isComplete`](cxaction/iscomplete.md) property of the action to [`true`](https://developer.apple.com/documentation/swift/true).

The [`CXCallAction`](cxcallaction.md) subclass is an abstract class that represents an action associated with a [`CXCall`](cxcall.md) object. The CallKit framework provides several concrete [`CXCallAction`](cxcallaction.md) subclasses to represent actions such as answering a call and putting a call on hold.

## Topics

### Creating an Action
- [init()](cxaction/init.md)
  Initializes a new telephony action.
- [init?(coder: NSCoder)](cxaction/init(coder:).md)
  Creates a new telephony action with data in an unarchiver.
### Accessing Action Attributes
- [var uuid: UUID](cxaction/uuid.md)
  The unique identifier for the action.
- [var isComplete: Bool](cxaction/iscomplete.md)
  A Boolean value that indicates whether the action has been performed by the provider.
- [var timeoutDate: Date](cxaction/timeoutdate.md)
  The time after which the action cannot be completed.
### Completing Actions
- [func fulfill()](cxaction/fulfill.md)
  Reports the successful execution of the action.
- [func fail()](cxaction/fail.md)
  Reports the failed execution of the action.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CXCallAction](cxcallaction.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CXCallAction](cxcallaction.md)
  A programmatic interface for objects that represent a telephony action associated with a call object.
- [class CXEndCallAction](cxendcallaction.md)
  An encapsulation of the act of ending a call.
- [class CXPlayDTMFCallAction](cxplaydtmfcallaction.md)
  An encapsulation of the act of playing a dual tone multifrequency (DTMF) sequence.
- [class CXSetGroupCallAction](cxsetgroupcallaction.md)
  An encapsulation of the act of grouping or ungrouping calls.
- [class CXSetHeldCallAction](cxsetheldcallaction.md)
  An encapsulation of the act of placing a call on hold or removing a call from hold.
- [class CXSetMutedCallAction](cxsetmutedcallaction.md)
  An encapsulation of the act of muting or unmuting a call.
- [class CXSetTranslatingCallAction](cxsettranslatingcallaction.md)
  An encapsulation of the act of translating a call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxaction)*