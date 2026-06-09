# AppEncryptionDeclaration

**Framework**: App Store Connect API  
**Kind**: dictionary

A declaration of an app’s use of encryption, required for export compliance and App Store submission.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object AppEncryptionDeclaration
```

## Topics

### Objects
- [object AppEncryptionDeclaration.Attributes](appencryptiondeclaration/attributes-data.dictionary.md)
  Attributes that describe an App Encryption Declarations resource.
- [object AppEncryptionDeclaration.Relationships](appencryptiondeclaration/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (AppEncryptionDeclaration.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `relationships` (AppEncryptionDeclaration.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

- [object AppEncryptionDeclarationCreateRequest](appencryptiondeclarationcreaterequest.md)
  The request body you use to create an app encryption declaration.
- [object AppEncryptionDeclarationDocument](appencryptiondeclarationdocument.md)
  An uploaded export compliance document supporting an app encryption declaration.
- [object AppEncryptionDeclarationDocumentCreateRequest](appencryptiondeclarationdocumentcreaterequest.md)
  The request body for uploading an encryption compliance document for an app.
- [object AppEncryptionDeclarationDocumentResponse](appencryptiondeclarationdocumentresponse.md)
  A response containing a single encryption compliance document for an app.
- [object AppEncryptionDeclarationDocumentUpdateRequest](appencryptiondeclarationdocumentupdaterequest.md)
  The request body you use to update an app encryption declaration document update request.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appencryptiondeclaration)*