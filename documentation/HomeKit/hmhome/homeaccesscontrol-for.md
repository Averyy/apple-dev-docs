# homeAccessControl(for:)

**Framework**: HomeKit  
**Kind**: method

Retrieves the access level of a user associated with the home.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func homeAccessControl(for user: HMUser) -> HMHomeAccessControl
```

#### Return Value

The access level associated with the user.

## Parameters

- `user`: The user whose access level you wish to retrieve.

## See Also

- [class HMHomeAccessControl](hmhomeaccesscontrol.md)
  The access privileges of a user associated with a home.
- [class HMAccessControl](hmaccesscontrol.md)
  An abstract superclass for accessing user privileges.
- [let HMUserFailedAccessoriesKey: String](hmuserfailedaccessorieskey.md)
  The key for retrieving details of what accessories failed to add or remove a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/homeaccesscontrol(for:))*