# Modify an app store version

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the App Store version for a specific app.

**Availability**:
- App Store Connect API 1.2+

## Mentions

- [App Store Connect API 3.3 release notes](./app-store-connect-api-3-3-release-notes.md)
- [Configuring alternative marketplaces and alternative marketplace apps](./configuring-alternative-marketplaces-and-alternative-marketplace-apps.md)

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store version resource ID from the [`List all app store versions for an app`](./get-v1-apps-_id_-appstoreversions.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppStoreVersionUpdateRequest`

## Responses

- `200` OK (`AppStoreVersionResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating and Modifying App Store Versions
- [Create an app store version](./post-v1-appstoreversions.md)
  Add a new App Store version or platform to an app.
- [Delete an app store version](./delete-v1-appstoreversions-_id_.md)
  Delete an app store version that is associated with an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appstoreversions-_id_)*