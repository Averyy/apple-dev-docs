# Upload an app encryption declaration document

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add an App Encryption Declaration Document to an existing App Encryption Declaration.

**Availability**:
- App Store Connect API 2.2+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarationDocuments`

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppEncryptionDeclarationDocumentCreateRequest`

## Responses

- `201` Created (`AppEncryptionDeclarationDocumentResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Uploading App Encryption Declaration Documents
- [Modify an app encryption declaration document](./patch-v1-appencryptiondeclarationdocuments-_id_.md)
  Commit an App Encryption Declaration Document after uploading it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appencryptiondeclarationdocuments)*