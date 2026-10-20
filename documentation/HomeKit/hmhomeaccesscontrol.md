# HMHomeAccessControl

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HMHomeAccessControl : HMAccessControl
```

## Topics

### Getting the Privileges of a User
- [var isAdministrator: Bool](./hmhomeaccesscontrol/isadministrator.md)
  Specifies if the user has administrative privileges for the home.

## Relationships

### Inherits From
- [HMAccessControl](./hmaccesscontrol.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Controlling user access
- [func homeAccessControl(for: HMUser) -> HMHomeAccessControl](./hmhome/homeaccesscontrol%28for%29.md)
  Retrieves the access level of a user associated with the home.
- [class HMAccessControl](./hmaccesscontrol.md)
  An abstract superclass for accessing user privileges.
- [let HMUserFailedAccessoriesKey: String](./hmuserfailedaccessorieskey.md)
  The key for retrieving details of what accessories failed to add or remove a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomeaccesscontrol)*