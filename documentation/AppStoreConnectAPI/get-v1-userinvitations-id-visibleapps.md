# List all apps visible to an invited user

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of apps that will be visible to a user with a pending invitation.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/userInvitations/{id}/visibleApps`

## Parameters

- `limit` (integer): Number of resources to return.
- `fields[apps]` ([string]): Fields to return for included related types.

## See Also

- [List visible app IDs for a user invitation](get-v1-userinvitations-_id_-relationships-visibleapps.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-userinvitations-_id_-visibleapps)*