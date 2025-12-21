# MobilePhotoIDDataRequest.Response.DocumentElements

**Framework**: ProximityReader  
**Kind**: struct

A type that contains the document elements from a successful photo ID data request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
struct DocumentElements
```

## Topics

### Structures
- [MobilePhotoIDDataRequest.Response.DocumentElements.IssuingAuthority](mobilephotoiddatarequest/response/documentelements-swift.struct/issuingauthority-swift.struct.md)
  A type that represents the state or government that issued the identity document.
### Instance Properties
- [var address: CNPostalAddress?](mobilephotoiddatarequest/response/documentelements-swift.struct/address.md)
  The photo ID holder’s address on record with the issuer.
- [let age: Int?](mobilephotoiddatarequest/response/documentelements-swift.struct/age.md)
  The photo ID holder’s age in years.
- [let ageAtLeastElements: [Int : Bool]](mobilephotoiddatarequest/response/documentelements-swift.struct/ageatleastelements.md)
  A dictionary of values that indicate whether the document holder is at least the specified age.
- [let dateOfBirth: DateComponents?](mobilephotoiddatarequest/response/documentelements-swift.struct/dateofbirth.md)
  The date of birth of the photo ID holder.
- [let documentExpirationDate: DateComponents?](mobilephotoiddatarequest/response/documentelements-swift.struct/documentexpirationdate.md)
  The document’s expiration date.
- [let documentIssueDate: DateComponents?](mobilephotoiddatarequest/response/documentelements-swift.struct/documentissuedate.md)
  The document’s issue date.
- [let documentNumber: String?](mobilephotoiddatarequest/response/documentelements-swift.struct/documentnumber.md)
  The document’s number, as defined by the document’s issuing authority.
- [let issuingAuthority: MobilePhotoIDDataRequest.Response.DocumentElements.IssuingAuthority?](mobilephotoiddatarequest/response/documentelements-swift.struct/issuingauthority-swift.property.md)
  The state or government that issued the identity document.
- [let nameComponents: PersonNameComponents?](mobilephotoiddatarequest/response/documentelements-swift.struct/namecomponents.md)
  The photo ID holder’s name components.
- [let portraitData: Data?](mobilephotoiddatarequest/response/documentelements-swift.struct/portraitdata.md)
  The portrait data of the photo ID holder on record with the issuer.
- [let sex: MobilePhotoIDDataRequest.Response.DocumentElements.Sex?](mobilephotoiddatarequest/response/documentelements-swift.struct/sex-swift.property.md)
  The photo ID holder’s sex.
### Enumerations
- [MobilePhotoIDDataRequest.Response.DocumentElements.Sex](mobilephotoiddatarequest/response/documentelements-swift.struct/sex-swift.enum.md)
  A type that represents the photo ID holder’s sex.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilephotoiddatarequest/response/documentelements-swift.struct)*