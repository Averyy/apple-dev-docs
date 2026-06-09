# Read the declaration document for an app encryption declaration

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read the associated document for a specific App Encryption Declaration.

**Availability**:
- App Store Connect API 2.2+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarations/6c2ddd3b-6d5e-4535-95f9-ece2c72c3848/appEncryptionDeclarationDocument
```

**Response**:

```json
{
  "data" : {
    "type" : "appEncryptionDeclarationDocuments",
    "id" : "e55c4bbe-a1b9-427c-99cf-fd8db5050fc9",
    "attributes" : {
      "fileSize" : 186110,
      "fileName" : "EncryptionDocumentation.pdf",
      "assetToken" : "Purple113/v4/11/d4/08/11d408a8-e57a-4541-60bb-4192a3722623/e55c4bbe-a1b9-427c-99cf-fd8db5050fc9_EncryptionDocumentation.pdf",
      "downloadUrl" : "https://misc-assets.itunes.apple.com/itunes-assets/Purple113/v4/11/d4/08/11d408a8-e57a-4541-60bb-4192a3722623/e55c4bbe-a1b9-427c-99cf-fd8db5050fc9_EncryptionDocumentation.pdf?accessKey=1675044398_3481250329993679798_NHHQ2xtrY2EX3gS7CwgTVEwFSvYg1NO1KRtGg7LiuZQ9ASafREyyovMKVIm2AyCwWPHfd%2Fquw%2BrXJsN%2BAWBgKsOkNwTmjqrLA86eFDTPrajcum4yoziAitV%2BIiYH34nIreiGrF%2BMqePA%2FOijcxCGQH6Tle4YNoSb7q0B1SFcgFHUwCi9ML6hQIJ7AJyf2d4uJSouqy8zUWBwRDHBl2B0kpMj6BOSdY%2B22PiKpFQXweQ%3D",
      "sourceFileChecksum" : "d228e04d46284ca195ad1ac7d13e269b",
      "uploadOperations" : null,
      "assetDeliveryState" : {
        "errors" : [ ],
        "warnings" : null,
        "state" : "COMPLETE"
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarationDocuments/e55c4bbe-a1b9-427c-99cf-fd8db5050fc9"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarations/6c2ddd3b-6d5e-4535-95f9-ece2c72c3848/appEncryptionDeclarationDocument"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarations/{id}/appEncryptionDeclarationDocument`

## Parameters

- `fields[appEncryptionDeclarationDocuments]` ([string]): Additional fields to include for each app encryption declaration document resource returned by the response.

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
- [Read the App ID of an App Encryption Declaration](get-v1-appencryptiondeclarations-_id_-relationships-app.md)
  Get the app id from a specific app encryption declaration.
- [Read a specific app encryption declaration document](get-v1-appencryptiondeclarationdocuments-_id_.md)
  Get detailed information about a specified App Encryption Declaration document.
- [Read the App ID of an App Encryption Declaration](get-v1-appencryptiondeclarations-_id_-relationships-app.md)
  Get the app id from a specific app encryption declaration.
- [Read the ID of the Document for an App Encryption Declaration](get-v1-appencryptiondeclarations-_id_-relationships-appencryptiondeclarationdocument.md)
  Get the document id associated with a specific app encryption declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appencryptiondeclarations-_id_-appencryptiondeclarationdocument)*