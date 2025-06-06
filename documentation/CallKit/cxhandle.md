# CXHandle

**Framework**: CallKit  
**Kind**: class

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

## Mentions

- [Making and receiving VoIP calls](making-and-receiving-voip-calls.md)

#### Overview

When the telephony provider receives an incoming call or the user starts an outgoing call, the other caller is identified by a [`CXHandle`](cxhandle.md) object. For a caller identified by a phone number, the handle type is [`CXHandle.HandleType.phoneNumber`](cxhandle/handletype/phonenumber.md) and the value is a sequence of digits. For a caller identified by an email address, the handle type is [`CXHandle.HandleType.emailAddress`](cxhandle/handletype/emailaddress.md) and the value is an email address. For a caller identified in any other way, the handle type is [`CXHandle.HandleType.generic`](cxhandle/handletype/generic.md) and the value typically follows some domain-specific format, such as a username, numeric ID, or URL.

## Topics

### Creating New Handles
- [init(type: CXHandle.HandleType, value: String)](cxhandle/init(type:value:).md)
  Initializes a new handle of a given type with the specified value.
### Accessing Handle Attributes
- [var type: CXHandle.HandleType](cxhandle/type.md)
  The type of the handle.
- [var value: String](cxhandle/value.md)
  The value of the handle.
### Constants
- [CXHandle.HandleType](cxhandle/handletype.md)
  The possible types of handles.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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

- [class CXCall](cxcall.md)
  A telephony call.
- [class CXCallObserver](cxcallobserver.md)
  A programmatic interface for an object that manages a list of active calls and observes call changes.
- [protocol CXCallObserverDelegate](cxcallobserverdelegate.md)
  A collection of methods the system calls when a call changes state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxhandle)*