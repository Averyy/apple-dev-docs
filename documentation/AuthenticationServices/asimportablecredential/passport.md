# ASImportableCredential.Passport

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

A representation of Passport as defined in the [Credential Exchange Format (CXF) specs](https://fidoalliance.org/specs/cx/cxf-v1.0-rd-20250313.html) This represents a passport document.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Passport
```

## Topics

### Initializers
- [init(issuingCountry: ASImportableEditableField?, passportType: ASImportableEditableField?, passportNumber: ASImportableEditableField?, nationalIdentificationNumber: ASImportableEditableField?, nationality: ASImportableEditableField?, fullName: ASImportableEditableField?, birthDate: ASImportableEditableField?, birthPlace: ASImportableEditableField?, sex: ASImportableEditableField?, issueDate: ASImportableEditableField?, expiryDate: ASImportableEditableField?, issuingAuthority: ASImportableEditableField?)](./passport/init%28issuingcountry,passporttype,passportnumber,nationalidentificationnumber,nationality,fullname,birthdate,birthplace,sex,issuedate,expirydate,issuingauthority%29.md)
### Instance Properties
- [var birthDate: ASImportableEditableField?](./passport/birthdate.md)
- [var birthPlace: ASImportableEditableField?](./passport/birthplace.md)
- [var expiryDate: ASImportableEditableField?](./passport/expirydate.md)
- [var fullName: ASImportableEditableField?](./passport/fullname.md)
- [var issueDate: ASImportableEditableField?](./passport/issuedate.md)
- [var issuingAuthority: ASImportableEditableField?](./passport/issuingauthority.md)
- [var issuingCountry: ASImportableEditableField?](./passport/issuingcountry.md)
- [var nationalIdentificationNumber: ASImportableEditableField?](./passport/nationalidentificationnumber.md)
- [var nationality: ASImportableEditableField?](./passport/nationality.md)
- [var passportNumber: ASImportableEditableField?](./passport/passportnumber.md)
- [var passportType: ASImportableEditableField?](./passport/passporttype.md)
- [var sex: ASImportableEditableField?](./passport/sex.md)

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/passport)*