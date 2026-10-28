# CXStartCallAction

**Framework**: CallKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface CXStartCallAction : CXCallAction
```

## Mentions

- [Making and receiving VoIP calls](./making-and-receiving-voip-calls.md)

## Overview

[`CXStartCallAction`](./cxstartcallaction.md) is a concrete subclass of [`CXCallAction`](./cxcallaction.md). When the user initiates an outgoing call, the provider sends [`provider(_:perform:)`](./cxproviderdelegate/provider%28_,perform%29-2lem5.md) to its delegate. The provider’s delegate calls the [`fulfill()`](./cxaction/fulfill%28%29.md) method to indicate that the action was successfully performed. To indicate that the call started at a time other than the current time, you can instead call the [`fulfill(withDateStarted:)`](./cxstartcallaction/fulfill%28withdatestarted%29.md).

## Topics

### Creating New Actions
- [init(call: UUID, handle: CXHandle)](./cxstartcallaction/init%28call,handle%29.md)
  Initializes a new action to start a call with the specified UUID to a recipient with the specified handle.
- [init?(coder: NSCoder)](./cxstartcallaction/init%28coder%29.md)
  Creates a new action to start a call with data in an unarchiver.
### Accessing Action Attributes
- [var isVideo: Bool](./cxstartcallaction/isvideo.md)
  A Boolean value that indicates whether the call is a video call.
- [var contactIdentifier: String?](./cxstartcallaction/contactidentifier.md)
  The identifier for the call recipient.
- [var handle: CXHandle](./cxstartcallaction/handle.md)
  The handle of the call recipient.
### Completing Actions
- [func fulfill(withDateStarted: Date)](./cxstartcallaction/fulfill%28withdatestarted%29.md)
  Reports the successful execution of the action at the specified time.
### Initializers
- [init(callUUID: UUID, handle: CXHandle)](./cxstartcallaction/init%28calluuid,handle%29.md)

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

### Outgoing calls
- [Sending End-to-End Encrypted VoIP Calls](./sending-end-to-end-encrypted-voip-calls.md)
  Initiate VoIP calls when your server can’t determine whether an outgoing notification is a request for a VoIP call due to metadata encryption.
- [class CXCallController](./cxcallcontroller.md)
  A programmatic interface for interacting with and observing calls.
- [class CXTransaction](./cxtransaction.md)
  An object that contains zero or more action objects for a call controller to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxstartcallaction)*