# MobilePhotoIDDataRequest.Element

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

A type that represents an element you can request from a photo ID.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct Element
```

## Topics

### Type Properties
- [static let address: MobilePhotoIDDataRequest.Element](./element/address.md)
  The photo ID holder’s address on record with the issuer.
- [static let age: MobilePhotoIDDataRequest.Element](./element/age.md)
  The photo ID holder’s age in years.
- [static let dateOfBirth: MobilePhotoIDDataRequest.Element](./element/dateofbirth.md)
  The date of birth of the photo ID holder.
- [static let documentExpirationDate: MobilePhotoIDDataRequest.Element](./element/documentexpirationdate.md)
  The document’s expiration date.
- [static let documentIssueDate: MobilePhotoIDDataRequest.Element](./element/documentissuedate.md)
  The document’s issue date.
- [static let documentNumber: MobilePhotoIDDataRequest.Element](./element/documentnumber.md)
  The document’s number, as defined by the document’s issuing authority.
- [static let familyName: MobilePhotoIDDataRequest.Element](./element/familyname.md)
  The photo ID holder’s family name or last name.
- [static let givenName: MobilePhotoIDDataRequest.Element](./element/givenname.md)
  The photo ID holder’s given name or first name.
- [static let issuingAuthority: MobilePhotoIDDataRequest.Element](./element/issuingauthority.md)
  The state or government that issued the identity document.
- [static let name: MobilePhotoIDDataRequest.Element](./element/name.md)
  The photo ID holder’s name.
- [static let portrait: MobilePhotoIDDataRequest.Element](./element/portrait.md)
  The picture of the photo ID holder on record with the issuer.
- [static let sex: MobilePhotoIDDataRequest.Element](./element/sex.md)
  The photo ID holder’s sex.
### Type Methods
- [static func ageAtLeast(Int) -> MobilePhotoIDDataRequest.Element](./element/ageatleast%28_%29.md)
  A Boolean value that indicates whether the photo ID holder’s age is at least the given age.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a data request
- [init(retainedElements: [MobilePhotoIDDataRequest.Element], nonRetainedElements: [MobilePhotoIDDataRequest.Element])](./init%28retainedelements,nonretainedelements%29.md)
  Returns a photo ID data request.
- [var nonRetainedElements: [MobilePhotoIDDataRequest.Element]](./nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than necessary to process the result in realtime.
- [var retainedElements: [MobilePhotoIDDataRequest.Element]](./retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilephotoiddatarequest/element)*