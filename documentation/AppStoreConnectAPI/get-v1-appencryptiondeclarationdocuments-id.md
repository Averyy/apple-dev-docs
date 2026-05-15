# Read a Specific App Encryption Declaration Document

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get detailed information about a specified App Encryption Declaration document.

**Availability**:
- App Store Connect API 2.2+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarationDocuments/e55c4bbe-a1b9-427c-99cf-fd8db5050fc9
```

**Response**:

```json
{  "data": {
    "type": "appEncryptionDeclarationDocuments",
    "id": "e55c4bbe-a1b9-427c-99cf-fd8db5050fc9",
    "attributes": {
      "fileSize": 186110,
      "fileName": "EncryptionDocumentation.pdf",
      "assetToken": "Purple113/v4/11/d4/08/11d408a8-e57a-4541-60bb-4192a3722623/e55c4bbe-a1b9-427c-99cf-fd8db5050fc9_EncryptionDocumentation.pdf",
      "downloadUrl": "https://misc-assets.itunes.apple.com/itunes-assets/Purple113/v4/11/d4/08/11d408a8-e57a-4541-60bb-4192a3722623/e55c4bbe-a1b9-427c-99cf-fd8db5050fc9_EncryptionDocumentation.pdf?accessKey=1675040844_8877869041959196296_dpXq9G7f4BF3oguy1BccshsmBYPlFP1xE4%2FenEAhRgymD2MPBYd1P%2BZopSavvkw3ZxuTRBGQwxHg4aBoWBl1UVFWOnW6nwI9Scivbm5vCk7GDEuVOImbEDaMYDC5Xxtag%2BVd2P4gDO7kdp%2FpPcnGLQFQ83RYrqfOqSqLstXnTwpbK9FPiQlGo1xIMZZYvLq5STbnREud24pbdmvvtUexlCoFuR7tjvpmRrlD0LGUUSs%3D",
      "sourceFileChecksum": "d228e04d46284ca195ad1ac7d13e269b",
      "uploadOperations": null,
      "assetDeliveryState": {
        "errors": [],
        "warnings": null,
        "state": "COMPLETE"
      }
    },
    "links": {
      "self": "https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarationDocuments/e55c4bbe-a1b9-427c-99cf-fd8db5050fc9"
    }
  },
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarationDocuments/e55c4bbe-a1b9-427c-99cf-fd8db5050fc9"
  }
}


```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarationDocuments/{id}`

## Parameters

- `fields[appEncryptionDeclarationDocuments]` ([string])

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
- [Read the Declaration Document for an App Encryption Declaration](get-v1-appencryptiondeclarations-_id_-appencryptiondeclarationdocument.md)
  Read the associated document for a specific App Encryption Declaration.
- [Read the App ID of an App Encryption Declaration](get-v1-appencryptiondeclarations-_id_-relationships-app.md)
  Get the app id from a specific app encryption declaration.
- [Read the ID of the Document for an App Encryption Declaration](get-v1-appencryptiondeclarations-_id_-relationships-appencryptiondeclarationdocument.md)
  Get the document id associated with a specific app encryption declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appencryptiondeclarationdocuments-_id_)*