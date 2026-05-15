# Read the ID of the Document for an App Encryption Declaration

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the document id associated with a specific app encryption declaration.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarations/{id}/relationships/appEncryptionDeclarationDocument`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List App Encryption Declarations`](get-v1-appencryptiondeclarations.md) response.

## See Also

- [List App Encryption Declarations](get-v1-appencryptiondeclarations.md)
  Find and list all available app encryption declarations.
- [Read App Encryption Declaration Information](get-v1-appencryptiondeclarations-_id_.md)
  Get information about a specific app encryption declaration.
- [Read an App’s Encryption Declarations](get-v1-apps-_id_-appencryptiondeclarations.md)
  Find and list all available app encryption declarations.
- [Read an App’s Encryption Declaration IDs](get-v1-apps-_id_-relationships-appencryptiondeclarations.md)
  Find and list all available app encryption declaration IDs for a specific app.
- [Read the App Information of an App Encryption Declaration](get-v1-appencryptiondeclarations-_id_-app.md)
  Get the app information from a specific app encryption declaration.
- [Read the App ID of an App Encryption Declaration](get-v1-appencryptiondeclarations-_id_-relationships-app.md)
  Get the app id from a specific app encryption declaration.
- [Read a Specific App Encryption Declaration Document](get-v1-appencryptiondeclarationdocuments-_id_.md)
  Get detailed information about a specified App Encryption Declaration document.
- [Read the Declaration Document for an App Encryption Declaration](get-v1-appencryptiondeclarations-_id_-appencryptiondeclarationdocument.md)
  Read the associated document for a specific App Encryption Declaration.
- [Read the App ID of an App Encryption Declaration](get-v1-appencryptiondeclarations-_id_-relationships-app.md)
  Get the app id from a specific app encryption declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appencryptiondeclarations-_id_-relationships-appencryptiondeclarationdocument)*