# List Invited Users

**Framework**: Enterprise Program API  
**Kind**: httpRequest

Get a list of pending invitations to join your team.

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/userInvitations`

## Parameters

- `fields[userInvitations]` ([string]): Fields to return for included related types.
- `limit` (integer): Number of resources to return.
- `sort` ([string]): Attributes by which to sort.
- `filter[roles]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[email]` ([string]): Attributes, relationships, and IDs by which to filter.

## See Also

- [Read user invitation information](read-userinvitation-information.md)
  Get information about a pending invitation to join your team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/list-invited-users)*