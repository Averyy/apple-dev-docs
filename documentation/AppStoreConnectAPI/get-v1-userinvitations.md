# List invited users

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of pending invitations to join your team.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/userInvitations`

## Parameters

- `fields[apps]` ([string]): Fields to return for included related types.
- `fields[userInvitations]` ([string]): Fields to return for included related types.
- `include` ([string]): Relationship data to include in the response.
- `limit` (integer): Number of resources to return.
- `sort` ([string]): Attributes by which to sort.
- `filter[roles]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[email]` ([string]): Attributes, relationships, and IDs by which to filter.
- `limit[visibleApps]` (integer): Number of included related resources to return.
- `filter[visibleApps]` ([string]): Number of included related resources to return.

## See Also

- [Read user invitation information](get-v1-userinvitations-_id_.md)
  Get information about a pending invitation to join your team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-userinvitations)*