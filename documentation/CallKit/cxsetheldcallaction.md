# CXSetHeldCallAction

**Framework**: CallKit  
**Kind**: class

An encapsulation of the act of placing a call on hold or removing a call from hold.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CXSetHeldCallAction
```

#### Overview

[`CXSetHeldCallAction`](cxsetheldcallaction.md) is a concrete subclass of [`CXCallAction`](cxcallaction.md).

When a caller places a call on hold, callers are unable to communicate with one another until the holding caller removes the call from hold. Placing a call on hold doesn’t end the call.

When the user or the system places a call on hold, the provider sends [`provider(_:perform:)`](cxproviderdelegate/provider(_:perform:)-947b1.md) to its delegate. The provider’s delegate calls the [`fulfill()`](cxaction/fulfill().md) method to indicate that the action was successfully performed.

## Topics

### Creating New Actions
- [init(call: UUID, onHold: Bool)](cxsetheldcallaction/init(call:onhold:).md)
  Initializes a new action for a call identified by a given UUID, as well as whether the call is on hold.
- [init?(coder: NSCoder)](cxsetheldcallaction/init(coder:).md)
  Creates a new action to place a call on hold with data in an unarchiver.
### Accessing Action Information
- [var isOnHold: Bool](cxsetheldcallaction/isonhold.md)
  A Boolean value that indicates whether the call is placed on hold.

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
- [class CXPlayDTMFCallAction](cxplaydtmfcallaction.md)
  An encapsulation of the act of playing a dual tone multifrequency (DTMF) sequence.
- [class CXSetGroupCallAction](cxsetgroupcallaction.md)
  An encapsulation of the act of grouping or ungrouping calls.
- [class CXSetMutedCallAction](cxsetmutedcallaction.md)
  An encapsulation of the act of muting or unmuting a call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxsetheldcallaction)*