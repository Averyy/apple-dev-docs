# MobilePhotoIDDataRequest.Response.DocumentElements

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

A type that contains the document elements from a successful photo ID data request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct DocumentElements
```

## Topics

### Structures
- [MobilePhotoIDDataRequest.Response.DocumentElements.IssuingAuthority](./documentelements-swift.struct/issuingauthority-swift.struct.md)
  A type that represents the state or government that issued the identity document.
### Instance Properties
- [var address: CNPostalAddress?](./documentelements-swift.struct/address.md)
  The photo ID holder’s address on record with the issuer.
- [let age: Int?](./documentelements-swift.struct/age.md)
  The photo ID holder’s age in years.
- [let ageAtLeastElements: [Int : Bool]](./documentelements-swift.struct/ageatleastelements.md)
  A dictionary of values that indicate whether the document holder is at least the specified age.
- [let dateOfBirth: DateComponents?](./documentelements-swift.struct/dateofbirth.md)
  The date of birth of the photo ID holder.
- [let documentExpirationDate: DateComponents?](./documentelements-swift.struct/documentexpirationdate.md)
  The document’s expiration date.
- [let documentIssueDate: DateComponents?](./documentelements-swift.struct/documentissuedate.md)
  The document’s issue date.
- [let documentNumber: String?](./documentelements-swift.struct/documentnumber.md)
  The document’s number, as defined by the document’s issuing authority.
- [let issuingAuthority: MobilePhotoIDDataRequest.Response.DocumentElements.IssuingAuthority?](./documentelements-swift.struct/issuingauthority-swift.property.md)
  The state or government that issued the identity document.
- [let name: MobileDocumentHolderName?](./documentelements-swift.struct/name.md)
  The photo ID holder’s name.
- [var nameComponents: PersonNameComponents?](./documentelements-swift.struct/namecomponents.md)
  The photo ID holder’s name components.
- [let portraitData: Data?](./documentelements-swift.struct/portraitdata.md)
  The portrait data of the photo ID holder on record with the issuer.
- [let sex: MobilePhotoIDDataRequest.Response.DocumentElements.Sex?](./documentelements-swift.struct/sex-swift.property.md)
  The photo ID holder’s sex.
### Enumerations
- [MobilePhotoIDDataRequest.Response.DocumentElements.Sex](./documentelements-swift.struct/sex-swift.enum.md)
  A type that represents the photo ID holder’s sex.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilephotoiddatarequest/response/documentelements-swift.struct)*