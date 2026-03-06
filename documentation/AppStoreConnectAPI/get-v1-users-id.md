# Read User Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a user on your team, such as name, roles, and app visibility.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/users/{id}`

## Parameters

- `fields[apps]` ([string]): Fields to return for included related types.
- `fields[users]` ([string]): Fields to return for included related types.
- `include` ([string]): Relationship data to include in the response.
- `limit[visibleApps]` (integer): Number of included related resources to return.

## See Also

- [List Users](get-v1-users.md)
  Get a list of the users on your team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-users-_id_)*