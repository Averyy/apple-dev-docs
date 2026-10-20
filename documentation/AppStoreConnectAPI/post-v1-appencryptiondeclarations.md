# Create an app encryption declaration

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add an app encryption delcaration for a specific app.

**Availability**:
- App Store Connect API 3.6+

## Mentions

- [App Store Connect API 3.6 release notes](./app-store-connect-api-3-6-release-notes.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarations`

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppEncryptionDeclarationCreateRequest`

## Responses

- `201` Created (`AppEncryptionDeclarationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Assigning App Encryption Declarations
- [Assign builds to an app encryption declaration](./post-v1-appencryptiondeclarations-_id_-relationships-builds.md)
  Assign one or more builds to an app encryption declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appencryptiondeclarations)*