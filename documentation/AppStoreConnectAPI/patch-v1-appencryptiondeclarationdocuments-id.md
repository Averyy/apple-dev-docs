# Modify an App Encryption Declaration Document

**Framework**: App Store Connect API  
**Kind**: httpRequest

Commit an App Encryption Declaration Document after uploading it.

**Availability**:
- App Store Connect API 2.2+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarationDocuments/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List App Encryption Declarations`](get-v1-appencryptiondeclarations.md) response, you will need to use the include `appEncryptionDeclarationDocument.`

## See Also

- [Upload an App Encryption Declaration Document](post-v1-appencryptiondeclarationdocuments.md)
  Add an App Encryption Declaration Document to an existing App Encryption Declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appencryptiondeclarationdocuments-_id_)*