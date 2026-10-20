# userIDNotEmailAddress

**Framework**: HomeKit  
**Kind**: property  
**Role**: Type Property

An error indicating the user’s ID is not a valid email address.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var userIDNotEmailAddress: HMError.Code { get }
```

## See Also

### Detecting user errors
- [static var userDeclinedAddingUser: HMError.Code](./userdeclinedaddinguser.md)
  An error indicating the user canceled the add user operation.
- [static var userDeclinedRemovingUser: HMError.Code](./userdeclinedremovinguser.md)
  An error indicating the user canceled the remove user operation.
- [static var userDeclinedInvite: HMError.Code](./userdeclinedinvite.md)
  An error indicating the user declined the invitation.
- [static var userManagementFailed: HMError.Code](./usermanagementfailed.md)
  A user management error not covered by the other errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/useridnotemailaddress)*