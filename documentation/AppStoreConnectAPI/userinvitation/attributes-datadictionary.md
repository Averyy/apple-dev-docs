# UserInvitation.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that describe a User Invitations resource.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object UserInvitation.Attributes
```

## Properties

- `email` (email): The email address of a pending user invitation. The email address must be valid to activate the account. It can be any email address, not necessarily one associated with an Apple Account.
- `firstName` (string): The first name of the user with the pending user invitation.
- `lastName` (string): The last name of the user with the pending user invitation.
- `roles` ([UserRole]): Assigned user roles that determine the user’s access to sections of App Store Connect and tasks they can perform.
- `expirationDate` (date-time): The expiration date of the pending invitation.
- `provisioningAllowed` (boolean): A Boolean value that indicates the user’s specified role allows access to the provisioning functionality on the Apple Developer website.
- `allAppsVisible` (boolean): A Boolean value that indicates whether a user has access to all apps available to the team.

## See Also

- [User Invitations](user-invitations.md)
  Email invitations to join your App Store Connect team.
- [object UserInvitation.Relationships](userinvitation/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/userinvitation/attributes-data.dictionary)*