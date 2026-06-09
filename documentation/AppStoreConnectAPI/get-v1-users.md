# List users

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of the users on your team.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/users`

## Parameters

- `fields[apps]` ([string]): Fields to return for included related types.
- `fields[users]` ([string]): Fields to return for included related types.
- `include` ([string]): Relationship data to include in the response.
- `limit` (integer): Number of resources to return.
- `sort` ([string]): Attributes by which to sort.
- `filter[roles]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[visibleApps]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[username]` ([string]): Attributes, relationships, and IDs by which to filter.
- `limit[visibleApps]` (integer): Number of included related resources to return.

## See Also

- [Read user information](get-v1-users-_id_.md)
  Get information about a user on your team, such as name, roles, and app visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-users)*