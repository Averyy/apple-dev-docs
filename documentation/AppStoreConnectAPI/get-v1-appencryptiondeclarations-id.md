# Read App Encryption Declaration Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific app encryption declaration.

**Availability**:
- App Store Connect API 1.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarations/69ab60b8-2f7a-91d4-e053-5b8c7c110c82
```

**Response**:

```json
{
  "data" : {
    "type" : "appEncryptionDeclarations",
    "id" : "69ab60b8-2f7a-91d4-e053-5b8c7c110c82",
    "attributes" : {
      "usesEncryption" : true,
      "exempt" : false,
      "containsProprietaryCryptography" : true,
      "containsThirdPartyCryptography" : false,
      "availableOnFrenchStore" : true,
      "platform" : "ios",
      "uploadedDate" : "2017-04-22T12:16:46-07:00",
      "documentUrl" : "https://misc-assets.itunes.apple.com/itunes-assets/Purple122/v4/d7/95/a7/d795a76e-3979-1f01-7bfb-5e5f2743af01/pr_source.pdf?accessKey=1674990162_6254129799175828264_uoh8Pzf0BlIzad3Lf9lhp9aqsz3vbNsz9anPfOVET3eE3Pifrb07%2BGcanQHmdwQVYMwkOx%2BZ1Wz7sralhjPgdp8vms9wLknEkuC1XU8HJY5%2Bok%2FOcMYjOnxYpThTYZ%2F9BhUkRjupYVAJ1trISCCgn7oa5y%2BVCFckt3q8eTwhdo0%3D",
      "documentName" : "ECDoc.pdf",
      "documentType" : "pdf",
      "appEncryptionDeclarationState" : "APPROVED",
      "codeValue" : "1c9a2aa8-d0f6-466a-b5dd-d87d881c18c6"
    },
    "relationships" : {
      "app" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarations/69ab60b8-2f7a-91d4-e053-5b8c7c110c82/relationships/app",
          "related" : "https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarations/69ab60b8-2f7a-91d4-e053-5b8c7c110c82/app"
        }
      },
      "builds" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarations/69ab60b8-2f7a-91d4-e053-5b8c7c110c82/relationships/builds"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarations/69ab60b8-2f7a-91d4-e053-5b8c7c110c82"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarations/69ab60b8-2f7a-91d4-e053-5b8c7c110c82"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarations/{id}`

## Parameters

- `fields[appEncryptionDeclarations]` ([string]): Fields to return for included related types.
- `fields[apps]` ([string]): Fields to return for included related types.
- `include` ([string]): Relationship data to include in the response.
- `fields[appEncryptionDeclarationDocuments]` ([string])
- `limit[builds]` (integer)
- `fields[builds]` ([string])

## See Also

- [List App Encryption Declarations](get-v1-appencryptiondeclarations.md)
  Find and list all available app encryption declarations.
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
- [Read the ID of the Document for an App Encryption Declaration](get-v1-appencryptiondeclarations-_id_-relationships-appencryptiondeclarationdocument.md)
  Get the document id associated with a specific app encryption declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appencryptiondeclarations-_id_)*