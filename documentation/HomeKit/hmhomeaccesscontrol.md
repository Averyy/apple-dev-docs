# HMHomeAccessControl

**Framework**: HomeKit  
**Kind**: class

The access privileges of a user associated with a home.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HMHomeAccessControl
```

## Topics

### Getting the Privileges of a User
- [var isAdministrator: Bool](hmhomeaccesscontrol/isadministrator.md)
  Specifies if the user has administrative privileges for the home.

## Relationships

### Inherits From
- [HMAccessControl](hmaccesscontrol.md)
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
- [class HMAccessControl](hmaccesscontrol.md)
  An abstract superclass for accessing user privileges.
- [let HMUserFailedAccessoriesKey: String](hmuserfailedaccessorieskey.md)
  The key for retrieving details of what accessories failed to add or remove a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomeaccesscontrol)*