# Read User Invitation Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a pending invitation to join your team.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/userInvitations/{id}`

## Parameters

- `fields[apps]` ([string]): Fields to return for included related types.
- `fields[userInvitations]` ([string]): Fields to return for included related types.
- `include` ([string]): Relationship data to include in the response.
- `limit[visibleApps]` (integer): Number of included related resources to return.

## See Also

- [List Invited Users](get-v1-userinvitations.md)
  Get a list of pending invitations to join your team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-userinvitations-_id_)*