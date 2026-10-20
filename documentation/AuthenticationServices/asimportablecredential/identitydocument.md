# ASImportableCredential.IdentityDocument

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

A representation of IdentityDocument as defined in the [Credential Exchange Format (CXF) specs](https://fidoalliance.org/specs/cx/cxf-v1.0-rd-20250313.html) This represents any kind of document that can be used for identification.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct IdentityDocument
```

## Topics

### Initializers
- [init(issuingCountry: ASImportableEditableField?, documentNumber: ASImportableEditableField?, identificationNumber: ASImportableEditableField?, nationality: ASImportableEditableField?, fullName: ASImportableEditableField?, birthDate: ASImportableEditableField?, birthPlace: ASImportableEditableField?, sex: ASImportableEditableField?, issueDate: ASImportableEditableField?, expiryDate: ASImportableEditableField?, issuingAuthority: ASImportableEditableField?)](./identitydocument/init%28issuingcountry,documentnumber,identificationnumber,nationality,fullname,birthdate,birthplace,sex,issuedate,expirydate,issuingauthority%29.md)
### Instance Properties
- [var birthDate: ASImportableEditableField?](./identitydocument/birthdate.md)
- [var birthPlace: ASImportableEditableField?](./identitydocument/birthplace.md)
- [var documentNumber: ASImportableEditableField?](./identitydocument/documentnumber.md)
- [var expiryDate: ASImportableEditableField?](./identitydocument/expirydate.md)
- [var fullName: ASImportableEditableField?](./identitydocument/fullname.md)
- [var identificationNumber: ASImportableEditableField?](./identitydocument/identificationnumber.md)
- [var issueDate: ASImportableEditableField?](./identitydocument/issuedate.md)
- [var issuingAuthority: ASImportableEditableField?](./identitydocument/issuingauthority.md)
- [var issuingCountry: ASImportableEditableField?](./identitydocument/issuingcountry.md)
- [var nationality: ASImportableEditableField?](./identitydocument/nationality.md)
- [var sex: ASImportableEditableField?](./identitydocument/sex.md)

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/identitydocument)*