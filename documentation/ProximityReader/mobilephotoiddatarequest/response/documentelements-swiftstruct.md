# MobilePhotoIDDataRequest.Response.DocumentElements

**Framework**: ProximityReader  
**Kind**: struct

A type that contains the document elements from a successful photo ID data request.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct DocumentElements
```

## Topics

### Structures
- [MobilePhotoIDDataRequest.Response.DocumentElements.IssuingAuthority](mobilephotoiddatarequest/response/documentelements-swift.struct/issuingauthority-swift.struct.md)
  A type that represents the state or government that issued the identity document.
### Operators
- [static func == (MobilePhotoIDDataRequest.Response.DocumentElements, MobilePhotoIDDataRequest.Response.DocumentElements) -> Bool](mobilephotoiddatarequest/response/documentelements-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
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
- [var hashValue: Int](mobilephotoiddatarequest/response/documentelements-swift.struct/hashvalue.md)
  The hash value.
- [let issuingAuthority: MobilePhotoIDDataRequest.Response.DocumentElements.IssuingAuthority?](mobilephotoiddatarequest/response/documentelements-swift.struct/issuingauthority-swift.property.md)
  The state or government that issued the identity document.
- [let nameComponents: PersonNameComponents?](mobilephotoiddatarequest/response/documentelements-swift.struct/namecomponents.md)
  The photo ID holder’s name components.
- [let portraitData: Data?](mobilephotoiddatarequest/response/documentelements-swift.struct/portraitdata.md)
  The portrait data of the photo ID holder on record with the issuer.
- [let sex: MobilePhotoIDDataRequest.Response.DocumentElements.Sex?](mobilephotoiddatarequest/response/documentelements-swift.struct/sex-swift.property.md)
  The photo ID holder’s sex.
### Instance Methods
- [func hash(into: inout Hasher)](mobilephotoiddatarequest/response/documentelements-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Enumerations
- [MobilePhotoIDDataRequest.Response.DocumentElements.Sex](mobilephotoiddatarequest/response/documentelements-swift.struct/sex-swift.enum.md)
  A type that represents the photo ID holder’s sex.
### Default Implementations
- [Equatable Implementations](mobilephotoiddatarequest/response/documentelements-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilephotoiddatarequest/response/documentelements-swift.struct)*