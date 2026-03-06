# UserInvitationCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that you set that describe the new resource.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object UserInvitationCreateRequest.Data.Attributes
```

## Properties

- `allAppsVisible` (boolean): A Boolean value that indicates whether a user has access to all apps available to the team.
- `email` (email) *(required)*: The email address of a pending user invitation. The email address must be valid to activate the account. It can be any email address, not necessarily one associated with an Apple Account.
- `firstName` (string) *(required)*: The user invitation recipient’s first name.
- `lastName` (string) *(required)*: The user invitation recipient’s last name.
- `provisioningAllowed` (boolean): A Boolean value that indicates the user’s specified role allows access to the provisioning functionality on the Apple Developer website.
- `roles` ([UserRole]) *(required)*: Assigned user roles that determine the user’s access to sections of App Store Connect and tasks they can perform.

## See Also

- [User Invitations](user-invitations.md)
  Email invitations to join your App Store Connect team.
- [object UserInvitationCreateRequest.Data.Relationships](userinvitationcreaterequest/data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/userinvitationcreaterequest/data-data.dictionary/attributes-data.dictionary)*