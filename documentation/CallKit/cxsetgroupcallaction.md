# CXSetGroupCallAction

**Framework**: CallKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface CXSetGroupCallAction : CXCallAction
```

## Overview

[`CXSetGroupCallAction`](./cxsetgroupcallaction.md) is a concrete subclass of [`CXCallAction`](./cxcallaction.md). When the user or the system groups a call with another call, the provider sends [`provider(_:perform:)`](./cxproviderdelegate/provider%28_,perform%29-9masw.md) to its delegate. The provider’s delegate calls the [`fulfill()`](./cxaction/fulfill%28%29.md) method to indicate that the action was successfully performed. A group call allows more than two recipients to simultaneously communicate with one another.

## Topics

### Creating New Actions
- [init(call: UUID, callUUIDToGroupWith: UUID?)](./cxsetgroupcallaction/init%28call,calluuidtogroupwith%29.md)
  Initializes a new action for a call identified by a given UUID, as well as a call to group with identified by another UUID.
- [init?(coder: NSCoder)](./cxsetgroupcallaction/init%28coder%29.md)
  Creates a new action to group calls with data in an unarchiver.
### Accessing Action Attributes
- [var callUUIDToGroupWith: UUID?](./cxsetgroupcallaction/calluuidtogroupwith.md)
  The unique identifier of the call to be grouped with the call associated with the receiver.
### Initializers
- [init(callUUID: UUID, callUUIDToGroupWith: UUID?)](./cxsetgroupcallaction/init%28calluuid,calluuidtogroupwith%29.md)

## Relationships

### Inherits From
- [CXCallAction](./cxcallaction.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Call-related actions
- [class CXAction](./cxaction.md)
  An abstract class that declares a programmatic interface for objects that represent a telephony action.
- [class CXCallAction](./cxcallaction.md)
  A programmatic interface for objects that represent a telephony action associated with a call object.
- [class CXEndCallAction](./cxendcallaction.md)
  An encapsulation of the act of ending a call.
- [class CXPlayDTMFCallAction](./cxplaydtmfcallaction.md)
  An encapsulation of the act of playing a dual tone multifrequency (DTMF) sequence.
- [class CXSetHeldCallAction](./cxsetheldcallaction.md)
  An encapsulation of the act of placing a call on hold or removing a call from hold.
- [class CXSetMutedCallAction](./cxsetmutedcallaction.md)
  An encapsulation of the act of muting or unmuting a call.
- [class CXSetTranslatingCallAction](./cxsettranslatingcallaction.md)
  An encapsulation of the act of translating a call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxsetgroupcallaction)*