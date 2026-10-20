# CXAnswerCallAction

**Framework**: CallKit  
**Kind**: class  
**Role**: Class

An encapsulation of the act of answering an incoming call.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CXAnswerCallAction
```

```objc
@interface CXAnswerCallAction : CXCallAction
```

#### Overview

[`CXAnswerCallAction`](./cxanswercallaction.md) is a concrete subclass of [`CXCallAction`](./cxcallaction.md).

When an incoming call is allowed by the system and approved by the user, the provider sends [`provider(_:perform:)`](./cxproviderdelegate/provider%28_,perform%29-h4in.md) to its delegate. The provider’s delegate calls the [`fulfill()`](./cxaction/fulfill%28%29.md) method to indicate that the action was successfully performed. To indicate that the call connected at a time other than the current time, you can instead call the [`fulfill(withDateConnected:)`](./cxanswercallaction/fulfill%28withdateconnected%29.md).

## Topics

### Completing Actions
- [func fulfill(withDateConnected: Date)](./cxanswercallaction/fulfill%28withdateconnected%29.md)
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

### Incoming calls
- [Responding to VoIP Notifications from PushKit](../PushKit/responding-to-voip-notifications-from-pushkit.md)
  Receive incoming Voice-over-IP (VoIP) push notifications and use them to display the system call interface to the user.
- [class CXCallUpdate](./cxcallupdate.md)
  An encapsulation of new and changed information about a call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxanswercallaction)*