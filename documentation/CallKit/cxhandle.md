# CXHandle

**Framework**: CallKit  
**Kind**: class  
**Role**: Class

A way to reach a call recipient, such as a phone number or email address.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CXHandle
```

```objc
@interface CXHandle : NSObject
```

## Mentions

- [Making and receiving VoIP calls](./making-and-receiving-voip-calls.md)

#### Overview

When the telephony provider receives an incoming call or the user starts an outgoing call, the other caller is identified by a [`CXHandle`](./cxhandle.md) object. For a caller identified by a phone number, the handle type is [`CXHandle.HandleType.phoneNumber`](./cxhandle/handletype/phonenumber.md) and the value is a sequence of digits. For a caller identified by an email address, the handle type is [`CXHandle.HandleType.emailAddress`](./cxhandle/handletype/emailaddress.md) and the value is an email address. For a caller identified in any other way, the handle type is [`CXHandle.HandleType.generic`](./cxhandle/handletype/generic.md) and the value typically follows some domain-specific format, such as a username, numeric ID, or URL.

## Topics

### Creating New Handles
- [init(type: CXHandle.HandleType, value: String)](./cxhandle/init%28type,value%29.md)
  Initializes a new handle of a given type with the specified value.
### Accessing Handle Attributes
- [var type: CXHandle.HandleType](./cxhandle/type.md)
  The type of the handle.
- [var value: String](./cxhandle/value.md)
  The value of the handle.
### Constants
- [CXHandle.HandleType](./cxhandle/handletype.md)
  The possible types of handles.
### Initializers
- [init?(coder: NSCoder)](./cxhandle/init%28coder%29.md)
### Comparing Handles
- [- isEqualToHandle:](./cxhandle/isequaltohandle_.md)
  Returns a Boolean value that indicates whether a given handle is equal to the receiver.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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

### Call information
- [class CXCall](./cxcall.md)
  A telephony call.
- [class CXCallObserver](./cxcallobserver.md)
  A programmatic interface for an object that manages a list of active calls and observes call changes.
- [protocol CXCallObserverDelegate](./cxcallobserverdelegate.md)
  A collection of methods the system calls when a call changes state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxhandle)*