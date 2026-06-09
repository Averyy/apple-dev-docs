# Read an app’s encryption declarations

**Framework**: App Store Connect API  
**Kind**: httpRequest

Find and list all available app encryption declarations.

**Availability**:
- App Store Connect API 3.0+

## Mentions

- [App Store Connect API 3.0 release notes](app-store-connect-api-3-0-release-notes.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/appEncryptionDeclarations`

## Parameters

- `fields[appEncryptionDeclarationDocuments]` ([string]): Additional fields to include for each app encryption declaration document resource returned by the response.
- `fields[appEncryptionDeclarations]` ([string]): Additional fields to include for each app encryption declaration resource returned by the response.
- `fields[apps]` ([string]): Additional fields to include for each app resource returned by the response.
- `fields[builds]` ([string]): Additional fields to include for each build resource returned by the response.
- `filter[builds]` ([string]): Filter the returned app encryption declarations by builds.
- `filter[platform]` ([string]): Filter the returned app encryption declarations by platform.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of app encryption declaration resources to return.
- `limit[builds]` (integer): The maximum number of related builds resources to return.

## See Also

- [List app encryption declarations](get-v1-appencryptiondeclarations.md)
  Find and list all available app encryption declarations.
- [Read app encryption declaration information](get-v1-appencryptiondeclarations-_id_.md)
  Get information about a specific app encryption declaration.
- [Read an app’s encryption declaration ids](get-v1-apps-_id_-relationships-appencryptiondeclarations.md)
  Find and list all available app encryption declaration IDs for a specific app.
- [Read the app information of an app encryption declaration](get-v1-appencryptiondeclarations-_id_-app.md)
  Get the app information from a specific app encryption declaration.
- [Read the App ID of an App Encryption Declaration](get-v1-appencryptiondeclarations-_id_-relationships-app.md)
  Get the app id from a specific app encryption declaration.
- [Read a specific app encryption declaration document](get-v1-appencryptiondeclarationdocuments-_id_.md)
  Get detailed information about a specified App Encryption Declaration document.
- [Read the declaration document for an app encryption declaration](get-v1-appencryptiondeclarations-_id_-appencryptiondeclarationdocument.md)
  Read the associated document for a specific App Encryption Declaration.
- [Read the App ID of an App Encryption Declaration](get-v1-appencryptiondeclarations-_id_-relationships-app.md)
  Get the app id from a specific app encryption declaration.
- [Read the ID of the Document for an App Encryption Declaration](get-v1-appencryptiondeclarations-_id_-relationships-appencryptiondeclarationdocument.md)
  Get the document id associated with a specific app encryption declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-appencryptiondeclarations)*