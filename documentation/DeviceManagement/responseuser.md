# ResponseUser

**Framework**: Device Management  
**Kind**: dictionary

The user in the organization.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ResponseUser
```

## Mentions

- [Managing Users](managing-users.md)

## Properties

- `clientUserId` (string): The unique identifier for a user in your organization.
- `email` (string): The user’s email address.
- `idHash` (string): The hash of the user’s unique store identifier. The `idHash` field is only present when the user has an associated Apple Account.
- `inviteCode` (string): The invitation code that associates an Apple Account to a user.
- `status` (string): The current status of the user in the organization.

## See Also

- [object Asset](asset.md)
  A product in the store.
- [object ResponseAsset](responseasset.md)
  The asset that the organization owns.
- [object Assignment](assignment.md)
  The asset assignment for a user or device.
- [object RequestUser](requestuser.md)
  The requested user in the organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/responseuser)*