# CXEndCallAction

**Framework**: CallKit  
**Kind**: class  
**Role**: Class

An encapsulation of the act of ending a call.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CXEndCallAction
```

```objc
@interface CXEndCallAction : CXCallAction
```

## Overview

[`CXEndCallAction`](./cxendcallaction.md) is a concrete subclass of [`CXCallAction`](./cxcallaction.md). When the user initiates an outgoing call, the provider sends [`provider(_:perform:)`](./cxproviderdelegate/provider%28_,perform%29-9a0m.md) to its delegate. The provider’s delegate calls the [`fulfill()`](./cxaction/fulfill%28%29.md) method to indicate that the action was successfully performed. To indicate that the call ended at a time other than the current time, you can instead call the [`fulfill(withDateEnded:)`](./cxendcallaction/fulfill%28withdateended%29.md)

## Topics

### Completing Actions
- [func fulfill(withDateEnded: Date)](./cxendcallaction/fulfill%28withdateended%29.md)
  Reports the successful execution of the action at the specified time.

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
- [class CXPlayDTMFCallAction](./cxplaydtmfcallaction.md)
  An encapsulation of the act of playing a dual tone multifrequency (DTMF) sequence.
- [class CXSetGroupCallAction](./cxsetgroupcallaction.md)
  An encapsulation of the act of grouping or ungrouping calls.
- [class CXSetHeldCallAction](./cxsetheldcallaction.md)
  An encapsulation of the act of placing a call on hold or removing a call from hold.
- [class CXSetMutedCallAction](./cxsetmutedcallaction.md)
  An encapsulation of the act of muting or unmuting a call.
- [class CXSetTranslatingCallAction](./cxsettranslatingcallaction.md)
  An encapsulation of the act of translating a call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxendcallaction)*