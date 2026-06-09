# Read the App ID of an App Encryption Declaration

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the app id from a specific app encryption declaration.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarations/{id}/relationships/app`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app encryption declaration resource ID from the [`List app encryption declarations`](get-v1-appencryptiondeclarations.md) response.

## See Also

- [List app encryption declarations](get-v1-appencryptiondeclarations.md)
  Find and list all available app encryption declarations.
- [Read app encryption declaration information](get-v1-appencryptiondeclarations-_id_.md)
  Get information about a specific app encryption declaration.
- [Read an app’s encryption declarations](get-v1-apps-_id_-appencryptiondeclarations.md)
  Find and list all available app encryption declarations.
- [Read an app’s encryption declaration ids](get-v1-apps-_id_-relationships-appencryptiondeclarations.md)
  Find and list all available app encryption declaration IDs for a specific app.
- [Read the app information of an app encryption declaration](get-v1-appencryptiondeclarations-_id_-app.md)
  Get the app information from a specific app encryption declaration.
- [Read a specific app encryption declaration document](get-v1-appencryptiondeclarationdocuments-_id_.md)
  Get detailed information about a specified App Encryption Declaration document.
- [Read the declaration document for an app encryption declaration](get-v1-appencryptiondeclarations-_id_-appencryptiondeclarationdocument.md)
  Read the associated document for a specific App Encryption Declaration.
- [Read the ID of the Document for an App Encryption Declaration](get-v1-appencryptiondeclarations-_id_-relationships-appencryptiondeclarationdocument.md)
  Get the document id associated with a specific app encryption declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appencryptiondeclarations-_id_-relationships-app)*