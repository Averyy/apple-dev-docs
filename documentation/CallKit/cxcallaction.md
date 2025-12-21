# CXCallAction

**Framework**: CallKit  
**Kind**: class

A programmatic interface for objects that represent a telephony action associated with a call object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CXCallAction
```

#### Overview

The CallKit framework provides the following concrete [`CXCallAction`](cxcallaction.md) subclasses.

| CXCallAction subclass | Description |
| --- | --- |
| [`CXAnswerCallAction`](cxanswercallaction.md) | Answers an incoming call. |
| [`CXStartCallAction`](cxstartcallaction.md) | Initiates an outgoing call. |
| [`CXEndCallAction`](cxendcallaction.md) | Ends a call. |
| [`CXSetHeldCallAction`](cxsetheldcallaction.md) | Places a call on hold or removes a call from hold. |
| [`CXSetGroupCallAction`](cxsetgroupcallaction.md) | Groups a call with another call or removes a call from a group. |
| [`CXSetMutedCallAction`](cxsetmutedcallaction.md) | Mutes or unmutes a call. |
| [`CXSetTranslatingCallAction`](cxsettranslatingcallaction.md) | Starts or stops call translation. |
| [`CXPlayDTMFCallAction`](cxplaydtmfcallaction.md) | Plays a DTMF (dual tone multifrequency) tone sequence on a call. |

To perform one or more actions, you add them to a new [`CXTransaction`](cxtransaction.md) object and pass the transaction to an instance of [`CXCallController`](cxcallcontroller.md) using the [`request(_:completion:)`](cxcallcontroller/request(_:completion:).md) method. After each action is performed by the telephony provider, the provider’s delegate calls either the [`CXCallAction`](cxcallaction.md) method, indicating that the action was successfully performed, or the [`CXCallAction`](cxcallaction.md) method, to indicate that an error occurred; both of these methods set the [`CXCallAction`](cxcallaction.md) property of the action to [`true`](https://developer.apple.com/documentation/Swift/true).

## Topics

### Creating New Call Actions
- [init(call: UUID)](cxcallaction/init(call:).md)
  Initializes a new action for a call identified by a given UUID.
- [init?(coder: NSCoder)](cxcallaction/init(coder:).md)
  Creates a new action for a call with data in an unarchiver.
### Accessing Call Action Attributes
- [var callUUID: UUID](cxcallaction/calluuid.md)
  The unique identifier for the call associated with the action.

## Relationships

### Inherits From
- [CXAction](cxaction.md)
### Inherited By
- [CXAnswerCallAction](cxanswercallaction.md)
- [CXEndCallAction](cxendcallaction.md)
- [CXPlayDTMFCallAction](cxplaydtmfcallaction.md)
- [CXSetGroupCallAction](cxsetgroupcallaction.md)
- [CXSetHeldCallAction](cxsetheldcallaction.md)
- [CXSetMutedCallAction](cxsetmutedcallaction.md)
- [CXSetTranslatingCallAction](cxsettranslatingcallaction.md)
- [CXStartCallAction](cxstartcallaction.md)
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

- [class CXAction](cxaction.md)
  An abstract class that declares a programmatic interface for objects that represent a telephony action.
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

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallaction)*