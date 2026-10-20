# Modify an app encryption declaration document

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Commit an App Encryption Declaration Document after uploading it.

**Availability**:
- App Store Connect API 2.2+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarationDocuments/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app encryption declaration document resource ID from the [`Read the declaration document for an app encryption declaration`](./get-v1-appencryptiondeclarations-_id_-appencryptiondeclarationdocument.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppEncryptionDeclarationDocumentUpdateRequest`

## Responses

- `200` OK (`AppEncryptionDeclarationDocumentResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Uploading App Encryption Declaration Documents
- [Upload an app encryption declaration document](./post-v1-appencryptiondeclarationdocuments.md)
  Add an App Encryption Declaration Document to an existing App Encryption Declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appencryptiondeclarationdocuments-_id_)*