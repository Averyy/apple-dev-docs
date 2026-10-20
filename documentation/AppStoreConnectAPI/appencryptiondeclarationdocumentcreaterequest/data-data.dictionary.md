# AppEncryptionDeclarationDocumentCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The request body you use to create an app encryption declaration document.

**Availability**:
- App Store Connect API 2.2+

## Declaration

```
object AppEncryptionDeclarationDocumentCreateRequest.Data
```

## Topics

### Objects
- [object AppEncryptionDeclarationDocumentCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.
- [object AppEncryptionDeclarationDocumentCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes that describe an app encryption declaration document create request resource.

## Properties

- `attributes` (AppEncryptionDeclarationDocumentCreateRequest.Data.Attributes) *(required)*
- `relationships` (AppEncryptionDeclarationDocumentCreateRequest.Data.Relationships) *(required)*
- `type` (string) *(required)*: **Allowed Values**: `appEncryptionDeclarationDocuments`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appencryptiondeclarationdocumentcreaterequest/data-data.dictionary)*