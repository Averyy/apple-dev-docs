# RequestUser

**Framework**: Device Management  
**Kind**: dictionary

The requested user in the organization.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object RequestUser
```

## Properties

- `clientUserId` (string) *(required)*: The unique identifier for a user in your organization.
- `email` (string): The email address for the user.
- `managedAppleId` (string): The Managed Apple Account for the user.

## See Also

- [object Asset](asset.md)
  A product in the store.
- [object ResponseAsset](responseasset.md)
  The asset that the organization owns.
- [object Assignment](assignment.md)
  The asset assignment for a user or device.
- [object ResponseUser](responseuser.md)
  The user in the organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/requestuser)*