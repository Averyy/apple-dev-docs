# AppEncryptionDeclarationDocument

**Framework**: App Store Connect API  
**Kind**: dictionary

An uploaded export compliance document supporting an app encryption declaration.

**Availability**:
- App Store Connect API 2.2+

## Declaration

```swift
object AppEncryptionDeclarationDocument
```

## Topics

### Objects
- [object AppEncryptionDeclarationDocument.Attributes](appencryptiondeclarationdocument/attributes-data.dictionary.md)
  Attributes that describe an app encryption declaration document resource.

## Properties

- `attributes` (AppEncryptionDeclarationDocument.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `type` (string) *(required)*

## See Also

- [object AppEncryptionDeclarationCreateRequest](appencryptiondeclarationcreaterequest.md)
  The request body you use to create an app encryption declaration.
- [object AppEncryptionDeclarationDocumentCreateRequest](appencryptiondeclarationdocumentcreaterequest.md)
  The request body for uploading an encryption compliance document for an app.
- [object AppEncryptionDeclarationDocumentResponse](appencryptiondeclarationdocumentresponse.md)
  A response containing a single encryption compliance document for an app.
- [object AppEncryptionDeclarationDocumentUpdateRequest](appencryptiondeclarationdocumentupdaterequest.md)
  The request body you use to update an app encryption declaration document update request.
- [object AppEncryptionDeclaration](appencryptiondeclaration.md)
  A declaration of an app’s use of encryption, required for export compliance and App Store submission.
- [object AppEncryptionDeclarationBuildsLinkagesRequest](appencryptiondeclarationbuildslinkagesrequest.md)
  A request body you use to add builds to an app encryption declaration.
- [object AppEncryptionDeclarationResponse](appencryptiondeclarationresponse.md)
  A response containing a single app encryption declaration.
- [object AppEncryptionDeclarationWithoutIncludesResponse](appencryptiondeclarationwithoutincludesresponse.md)
  A response containing a single encryption declaration, without related resources.
- [object AppEncryptionDeclarationsResponse](appencryptiondeclarationsresponse.md)
  A response containing a list of encryption declarations for an app.
- [type AppEncryptionDeclarationState](appencryptiondeclarationstate.md)
  Strings that represent the review or acceptance status of an app encryption declaration submitted to Apple.
- [object AppEncryptionDeclarationAppEncryptionDeclarationDocumentLinkageResponse](appencryptiondeclarationappencryptiondeclarationdocumentlinkageresponse.md)
- [object AppEncryptionDeclarationAppLinkageResponse](appencryptiondeclarationapplinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appencryptiondeclarationdocument)*