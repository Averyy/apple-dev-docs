# CXCallUpdate

**Framework**: CallKit  
**Kind**: class

An encapsulation of new and changed information about a call.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CXCallUpdate
```

## Mentions

- [Making and receiving VoIP calls](making-and-receiving-voip-calls.md)

#### Overview

[`CXCallUpdate`](cxcallupdate.md) objects are used by the system to communicate changes to calls over time. Not every property on a [`CXCallUpdate`](cxcallupdate.md) object must be set each time, as each object includes only new and changed information. For example, when a call is started, only some properties may be known and included in the first [`CXCallUpdate`](cxcallupdate.md) object sent to the system, such as [`localizedCallerName`](cxcallupdate/localizedcallername.md). Later in the same call, other properties may change; for example, a call may be upgraded from audio only to audio and video, which would be reflected by a new [`CXCallUpdate`](cxcallupdate.md) object with its [`hasVideo`](cxcallupdate/hasvideo.md) property set to [`true`](https://developer.apple.com/documentation/swift/true).

When an incoming call is received, you construct a [`CXCallUpdate`](cxcallupdate.md) object specifying a [`localizedCallerName`](cxcallupdate/localizedcallername.md) and pass that to the [`reportNewIncomingCall(with:update:completion:)`](cxprovider/reportnewincomingcall(with:update:completion:).md) method to notify the telephony provider.

When an active call is updated, you construct a [`CXCallUpdate`](cxcallupdate.md) object specifying any updated information and pass that to the [`reportCall(with:updated:)`](cxprovider/reportcall(with:updated:).md) method. For example, if a user changes their contact information during a call, you could notify the telephony provider of this change using a new [`CXCallUpdate`](cxcallupdate.md) object with the new value set to its [`remoteHandle`](cxcallupdate/remotehandle.md) property.

## Topics

### Accessing Call Update Attributes
- [var localizedCallerName: String?](cxcallupdate/localizedcallername.md)
  The localized name of the caller.
- [var remoteHandle: CXHandle?](cxcallupdate/remotehandle.md)
  The handle for the remote party (for an incoming call, this is the caller; for an outgoing call, this is the callee).
- [var hasVideo: Bool](cxcallupdate/hasvideo.md)
  A Boolean value that indicates whether the call includes video in addition to audio.
- [var supportsGrouping: Bool](cxcallupdate/supportsgrouping.md)
  A Boolean value that indicates whether the call can be grouped with other calls.
- [var supportsUngrouping: Bool](cxcallupdate/supportsungrouping.md)
  A Boolean value that indicates whether the call can be ungrouped from other calls.
- [var supportsHolding: Bool](cxcallupdate/supportsholding.md)
  A Boolean value that indicates whether the call can be placed on hold or removed from hold.
- [var supportsDTMF: Bool](cxcallupdate/supportsdtmf.md)
  A Boolean value that indicates whether the call can send DTMF (dual tone multifrequency) tones via hard pause digits or in-call keypad entries.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Responding to VoIP Notifications from PushKit](../PushKit/responding-to-voip-notifications-from-pushkit.md)
  Receive incoming Voice-over-IP (VoIP) push notifications and use them to display the system call interface to the user.
- [class CXAnswerCallAction](cxanswercallaction.md)
  An encapsulation of the act of answering an incoming call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallupdate)*