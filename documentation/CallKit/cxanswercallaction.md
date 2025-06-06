# CXAnswerCallAction

**Framework**: CallKit  
**Kind**: class

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

#### Overview

[`CXAnswerCallAction`](cxanswercallaction.md) is a concrete subclass of [`CXCallAction`](cxcallaction.md).

When an incoming call is allowed by the system and approved by the user, the provider sends [`provider(_:perform:)`](cxproviderdelegate/provider(_:perform:)-h4in.md) to its delegate. The provider’s delegate calls the [`fulfill()`](cxaction/fulfill().md) method to indicate that the action was successfully performed. To indicate that the call connected at a time other than the current time, you can instead call the [`fulfill(withDateConnected:)`](cxanswercallaction/fulfill(withdateconnected:).md).

## Topics

### Completing Actions
- [func fulfill(withDateConnected: Date)](cxanswercallaction/fulfill(withdateconnected:).md)
  Reports the successful execution of the action at the specified time.

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

- [Responding to VoIP Notifications from PushKit](../PushKit/responding-to-voip-notifications-from-pushkit.md)
  Receive incoming Voice-over-IP (VoIP) push notifications and use them to display the system call interface to the user.
- [class CXCallUpdate](cxcallupdate.md)
  An encapsulation of new and changed information about a call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxanswercallaction)*