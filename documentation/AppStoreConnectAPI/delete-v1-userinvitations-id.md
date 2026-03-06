# Cancel a User Invitation

**Framework**: App Store Connect API  
**Kind**: httpRequest

Cancel a pending invitation for a user to join your team.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/userInvitations/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## See Also

- [Invite a User](post-v1-userinvitations.md)
  Invite a user with assigned user roles to join your team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-userinvitations-_id_)*