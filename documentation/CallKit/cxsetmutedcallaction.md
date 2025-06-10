# CXSetMutedCallAction

**Framework**: CallKit  
**Kind**: class

An encapsulation of the act of muting or unmuting a call.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CXSetMutedCallAction
```

#### Overview

[`CXSetMutedCallAction`](cxsetmutedcallaction.md) is a concrete subclass of [`CXCallAction`](cxcallaction.md). When the user or the system mutes a call, the provider sends [`provider(_:perform:)`](cxproviderdelegate/provider(_:perform:)-4u3yu.md) to its delegate. The provider’s delegate calls the [`fulfill()`](cxaction/fulfill().md) method to indicate that the action was successfully performed. When a caller mutes a call, that caller is unable to communicate with other callers until they unmute the call. A muted caller still receives communication from other unmuted callers.

## Topics

### Creating New Actions
- [convenience init(call: UUID, muted: Bool)](cxsetmutedcallaction/init(call:muted:).md)
  Initializes a new action for a call identified by a given UUID, as well as whether the call is muted.
- [init?(coder: NSCoder)](cxsetmutedcallaction/init(coder:).md)
  Creates a new action for a call with data in an unarchiver.
### Accessing Action Attributes
- [var isMuted: Bool](cxsetmutedcallaction/ismuted.md)
  A Boolean value that indicates whether the call is muted.

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
- [class CXSetHeldCallAction](cxsetheldcallaction.md)
  An encapsulation of the act of placing a call on hold or removing a call from hold.
- [class CXSetTranslatingCallAction](cxsettranslatingcallaction.md)
  An encapsulation of the act of translating a call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxsetmutedcallaction)*