# CXStartCallAction

**Framework**: CallKit  
**Kind**: class

An encapsulation of the act of initiating an outgoing call.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CXStartCallAction
```

## Mentions

- [Making and receiving VoIP calls](making-and-receiving-voip-calls.md)

#### Overview

[`CXStartCallAction`](cxstartcallaction.md) is a concrete subclass of [`CXCallAction`](cxcallaction.md). When the user initiates an outgoing call, the provider sends [`provider(_:perform:)`](cxproviderdelegate/provider(_:perform:)-2lem5.md) to its delegate. The provider’s delegate calls the [`fulfill()`](cxaction/fulfill().md) method to indicate that the action was successfully performed. To indicate that the call started at a time other than the current time, you can instead call the [`fulfill(withDateStarted:)`](cxstartcallaction/fulfill(withdatestarted:).md).

## Topics

### Creating New Actions
- [init(call: UUID, handle: CXHandle)](cxstartcallaction/init(call:handle:).md)
  Initializes a new action to start a call with the specified UUID to a recipient with the specified handle.
- [init?(coder: NSCoder)](cxstartcallaction/init(coder:).md)
  Creates a new action to start a call with data in an unarchiver.
### Accessing Action Attributes
- [var isVideo: Bool](cxstartcallaction/isvideo.md)
  A Boolean value that indicates whether the call is a video call.
- [var contactIdentifier: String?](cxstartcallaction/contactidentifier.md)
  The identifier for the call recipient.
- [var handle: CXHandle](cxstartcallaction/handle.md)
  The handle of the call recipient.
### Completing Actions
- [func fulfill(withDateStarted: Date)](cxstartcallaction/fulfill(withdatestarted:).md)
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

- [Sending End-to-End Encrypted VoIP Calls](sending-end-to-end-encrypted-voip-calls.md)
  Initiate VoIP calls when your server can’t determine whether an outgoing notification is a request for a VoIP call due to metadata encryption.
- [class CXCallController](cxcallcontroller.md)
  A programmatic interface for interacting with and observing calls.
- [class CXTransaction](cxtransaction.md)
  An object that contains zero or more action objects for a call controller to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxstartcallaction)*