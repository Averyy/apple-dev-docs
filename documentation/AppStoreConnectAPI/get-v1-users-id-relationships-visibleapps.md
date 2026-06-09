# Get all visible app resource ids for a user

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of app resource IDs to which a user on your team has access.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/users/{id}/relationships/visibleApps`

## Parameters

- `limit` (integer): Number of resources to return.

## See Also

- [List all apps visible to a user](get-v1-users-_id_-visibleapps.md)
  Get a list of apps that a user on your team can view.
- [Add visible apps to a user](post-v1-users-_id_-relationships-visibleapps.md)
  Give a user on your team access to one or more apps.
- [Replace the list of visible apps for a user](patch-v1-users-_id_-relationships-visibleapps.md)
  Replace the list of apps a user on your team can see.
- [Remove visible apps from a user](delete-v1-users-_id_-relationships-visibleapps.md)
  Remove a user on your team’s access to one or more apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-users-_id_-relationships-visibleapps)*