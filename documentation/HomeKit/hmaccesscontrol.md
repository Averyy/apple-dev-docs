# HMAccessControl

**Framework**: HomeKit  
**Kind**: class

An abstract superclass for accessing user privileges.

**Availability**:
- iOS 11.2+
- iPadOS 11.2+
- Mac Catalyst 11.2+
- tvOS 11.2+
- visionOS 1.0+
- watchOS 4.2+

## Declaration

```swift
class HMAccessControl
```

#### Overview

Use a concrete subclass, like [`HMHomeAccessControl`](hmhomeaccesscontrol.md), instead.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [HMHomeAccessControl](hmhomeaccesscontrol.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func homeAccessControl(for: HMUser) -> HMHomeAccessControl](hmhome/homeaccesscontrol(for:).md)
  Retrieves the access level of a user associated with the home.
- [class HMHomeAccessControl](hmhomeaccesscontrol.md)
  The access privileges of a user associated with a home.
- [let HMUserFailedAccessoriesKey: String](hmuserfailedaccessorieskey.md)
  The key for retrieving details of what accessories failed to add or remove a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccesscontrol)*