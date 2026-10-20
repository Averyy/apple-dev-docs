# Assign the app encryption declaration for a build

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Assign an app encryption declaration to a build.

**Availability**:
- App Store Connect API 1.0+

> **Deprecated**: Use [`Modify a build`](./patch-v1-builds-_id_.md) to update the relationship to an app encryption declaration instead.

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/builds/{id}/relationships/appEncryptionDeclaration`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## Request Body

**Content-Type**: `application/json`  
**Type**: `BuildAppEncryptionDeclarationLinkageRequest`

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Modifying Builds
- [Modify a build](./patch-v1-builds-_id_.md)
  Expire a build or change its encryption exemption setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-builds-_id_-relationships-appencryptiondeclaration)*