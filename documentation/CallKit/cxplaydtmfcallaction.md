# CXPlayDTMFCallAction

**Framework**: CallKit  
**Kind**: class

An encapsulation of the act of playing a dual tone multifrequency (DTMF) sequence.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CXPlayDTMFCallAction
```

#### Overview

[`CXPlayDTMFCallAction`](cxplaydtmfcallaction.md) is a concrete subclass of [`CXCallAction`](cxcallaction.md). Whenever digits are transmitted during a call, whether from a user interacting with a number pad or following a hard or soft pause, the provider sends [`provider(_:perform:)`](cxproviderdelegate/provider(_:perform:)-4htxt.md) to its delegate. The provider’s delegate calls the [`fulfill()`](cxaction/fulfill().md) method to indicate that the action was successfully performed.

The provider sends [`provider(_:perform:)`](cxproviderdelegate/provider(_:perform:)-4htxt.md) for successive actions only after the current action is fulfilled. When interacting with the number pad, each entered digit constitutes its own action. Digits following a hard or soft pause, however, are passed to [`provider(_:perform:)`](cxproviderdelegate/provider(_:perform:)-4htxt.md) as a single string of digits. For example, if a user taps the 4 button on the number pad, followed by the 2 button, the delegate is sent [`provider(_:perform:)`](cxproviderdelegate/provider(_:perform:)-4htxt.md) for the digit `4` and waits for the action to be fulfilled; after the action is fulfilled, the delegate is sent [`provider(_:perform:)`](cxproviderdelegate/provider(_:perform:)-4htxt.md) for the digit `2`.

CallKit automatically plays the corresponding DTMF frequencies for any digits transmitted over a call. The app is responsible for managing the timing and handling of digits as part of fulfilling the action.

## Topics

### Creating New Actions
- [init(call: UUID, digits: String, type: CXPlayDTMFCallAction.ActionType)](cxplaydtmfcallaction/init(call:digits:type:).md)
  Initializes a new action for a call identified by a given UUID, as well as a specified type and sequence of digits.
- [init?(coder: NSCoder)](cxplaydtmfcallaction/init(coder:).md)
  Creates a new action to play dual-tone multifrequency (DTMF) tones with data in an unarchiver.
### Accessing Action Information
- [var digits: String](cxplaydtmfcallaction/digits.md)
  The digits tapped by the user into the in-call keypad or included in the dial string.
- [var type: CXPlayDTMFCallAction.ActionType](cxplaydtmfcallaction/type.md)
  The type of the call action.
### Constants
- [CXPlayDTMFCallAction.ActionType](cxplaydtmfcallaction/actiontype.md)
  The types of events that generate dial tones.

## Relationships

### Inherits From
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

- [class CXAction](cxaction.md)
  An abstract class that declares a programmatic interface for objects that represent a telephony action.
- [class CXCallAction](cxcallaction.md)
  A programmatic interface for objects that represent a telephony action associated with a call object.
- [class CXEndCallAction](cxendcallaction.md)
  An encapsulation of the act of ending a call.
- [class CXSetGroupCallAction](cxsetgroupcallaction.md)
  An encapsulation of the act of grouping or ungrouping calls.
- [class CXSetHeldCallAction](cxsetheldcallaction.md)
  An encapsulation of the act of placing a call on hold or removing a call from hold.
- [class CXSetMutedCallAction](cxsetmutedcallaction.md)
  An encapsulation of the act of muting or unmuting a call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxplaydtmfcallaction)*