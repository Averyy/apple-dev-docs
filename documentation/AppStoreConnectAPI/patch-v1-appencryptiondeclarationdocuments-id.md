# Modify an app encryption declaration document

**Framework**: App Store Connect API  
**Kind**: httpRequest

Commit an App Encryption Declaration Document after uploading it.

**Availability**:
- App Store Connect API 2.2+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarationDocuments/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app encryption declaration document resource ID from the [`Read the declaration document for an app encryption declaration`](get-v1-appencryptiondeclarations-_id_-appencryptiondeclarationdocument.md) response.

## See Also

- [Upload an app encryption declaration document](post-v1-appencryptiondeclarationdocuments.md)
  Add an App Encryption Declaration Document to an existing App Encryption Declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appencryptiondeclarationdocuments-_id_)*