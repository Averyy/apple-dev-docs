# List All Apps Visible to a User

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of apps that a user on your team can view.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/users/{id}/visibleApps`

## Parameters

- `limit` (integer): Number of resources to return.
- `fields[apps]` ([string]): Fields to return for included related types.

## See Also

- [Get All Visible App Resource IDs for a User](get-v1-users-_id_-relationships-visibleapps.md)
  Get a list of app resource IDs to which a user on your team has access.
- [Add Visible Apps to a User](post-v1-users-_id_-relationships-visibleapps.md)
  Give a user on your team access to one or more apps.
- [Replace the List of Visible Apps for a User](patch-v1-users-_id_-relationships-visibleapps.md)
  Replace the list of apps a user on your team can see.
- [Remove Visible Apps from a User](delete-v1-users-_id_-relationships-visibleapps.md)
  Remove a user on your team’s access to one or more apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-users-_id_-visibleapps)*