# CXSetGroupCallAction

**Framework**: CallKit  
**Kind**: class

An encapsulation of the act of grouping or ungrouping calls.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CXSetGroupCallAction
```

#### Overview

[`CXSetGroupCallAction`](cxsetgroupcallaction.md) is a concrete subclass of [`CXCallAction`](cxcallaction.md). When the user or the system groups a call with another call, the provider sends [`provider(_:perform:)`](cxproviderdelegate/provider(_:perform:)-9masw.md) to its delegate. The provider’s delegate calls the [`fulfill()`](cxaction/fulfill().md) method to indicate that the action was successfully performed. A group call allows more than two recipients to simultaneously communicate with one another.

## Topics

### Creating New Actions
- [init(call: UUID, callUUIDToGroupWith: UUID?)](cxsetgroupcallaction/init(call:calluuidtogroupwith:).md)
  Initializes a new action for a call identified by a given UUID, as well as a call to group with identified by another UUID.
- [init?(coder: NSCoder)](cxsetgroupcallaction/init(coder:).md)
  Creates a new action to group calls with data in an unarchiver.
### Accessing Action Attributes
- [var callUUIDToGroupWith: UUID?](cxsetgroupcallaction/calluuidtogroupwith.md)
  The unique identifier of the call to be grouped with the call associated with the receiver.

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
- [class CXSetHeldCallAction](cxsetheldcallaction.md)
  An encapsulation of the act of placing a call on hold or removing a call from hold.
- [class CXSetMutedCallAction](cxsetmutedcallaction.md)
  An encapsulation of the act of muting or unmuting a call.
- [class CXSetTranslatingCallAction](cxsettranslatingcallaction.md)
  An encapsulation of the act of translating a call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxsetgroupcallaction)*