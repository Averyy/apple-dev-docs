# Assign builds to an app encryption declaration

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Assign one or more builds to an app encryption declaration.

**Availability**:
- App Store Connect API 1.0+ - Deprecated in 2.4

> **Deprecated**: Use [`Modify a build`](./patch-v1-builds-_id_.md) to update the relationship to an app encryption declaration instead.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarations/{id}/relationships/builds`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app encryption declaration resource ID from the [`List app encryption declarations`](./get-v1-appencryptiondeclarations.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppEncryptionDeclarationBuildsLinkagesRequest`

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

### Assigning App Encryption Declarations
- [Create an app encryption declaration](./post-v1-appencryptiondeclarations.md)
  Add an app encryption delcaration for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appencryptiondeclarations-_id_-relationships-builds)*