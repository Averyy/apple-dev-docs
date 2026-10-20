# Delete an end user license agreement

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete the custom end user license agreement that is associated with an app.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/{id}`

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

### Creating, Modifying, and Deleting an EULA
- [Create an end user license agreement](./post-v1-enduserlicenseagreements.md)
  Add a custom end user license agreement (EULA) to an app and configure the territories to which it applies.
- [Modify an end user license agreement](./patch-v1-enduserlicenseagreements-_id_.md)
  Update the text or territories for your custom end user license agreement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-enduserlicenseagreements-_id_)*