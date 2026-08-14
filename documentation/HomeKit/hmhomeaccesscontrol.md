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
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func homeAccessControl(for: HMUser) -> HMHomeAccessControl](hmhome/homeaccesscontrol(for:).md)
  Retrieves the access level of a user associated with the home.
- [class HMAccessControl](hmaccesscontrol.md)
  An abstract superclass for accessing user privileges.
- [let HMUserFailedAccessoriesKey: String](hmuserfailedaccessorieskey.md)
  The key for retrieving details of what accessories failed to add or remove a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomeaccesscontrol)*