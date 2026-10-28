# Delete a profile

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete a provisioning profile that is used for app development or distribution.

**Availability**:
- App Store Connect API 1.1+

## Discussion

You can delete provisioning profiles, and may wish to do so if they are expiring or obsolete.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/profiles/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating and Deleting Provisioning Profiles
- [Create a profile](./post-v1-profiles.md)
  Create a new provisioning profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-profiles-_id_)*