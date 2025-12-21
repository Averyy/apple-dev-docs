# MobilePhotoIDDataRequest.Element

**Framework**: ProximityReader  
**Kind**: struct

A type that represents an element you can request from a photo ID.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Element
```

## Topics

### Type Properties
- [static let address: MobilePhotoIDDataRequest.Element](mobilephotoiddatarequest/element/address.md)
  The photo ID holder’s address on record with the issuer.
- [static let age: MobilePhotoIDDataRequest.Element](mobilephotoiddatarequest/element/age.md)
  The photo ID holder’s age in years.
- [static let dateOfBirth: MobilePhotoIDDataRequest.Element](mobilephotoiddatarequest/element/dateofbirth.md)
  The date of birth of the photo ID holder.
- [static let documentExpirationDate: MobilePhotoIDDataRequest.Element](mobilephotoiddatarequest/element/documentexpirationdate.md)
  The document’s expiration date.
- [static let documentIssueDate: MobilePhotoIDDataRequest.Element](mobilephotoiddatarequest/element/documentissuedate.md)
  The document’s issue date.
- [static let documentNumber: MobilePhotoIDDataRequest.Element](mobilephotoiddatarequest/element/documentnumber.md)
  The document’s number, as defined by the document’s issuing authority.
- [static let familyName: MobilePhotoIDDataRequest.Element](mobilephotoiddatarequest/element/familyname.md)
  The photo ID holder’s family name or last name.
- [static let givenName: MobilePhotoIDDataRequest.Element](mobilephotoiddatarequest/element/givenname.md)
  The photo ID holder’s given name or first name.
- [static let issuingAuthority: MobilePhotoIDDataRequest.Element](mobilephotoiddatarequest/element/issuingauthority.md)
  The state or government that issued the identity document.
- [static let portrait: MobilePhotoIDDataRequest.Element](mobilephotoiddatarequest/element/portrait.md)
  The picture of the photo ID holder on record with the issuer.
- [static let sex: MobilePhotoIDDataRequest.Element](mobilephotoiddatarequest/element/sex.md)
  The photo ID holder’s sex.
### Type Methods
- [static func ageAtLeast(Int) -> MobilePhotoIDDataRequest.Element](mobilephotoiddatarequest/element/ageatleast(_:).md)
  A Boolean value that indicates whether the photo ID holder’s age is at least the given age.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(retainedElements: [MobilePhotoIDDataRequest.Element], nonRetainedElements: [MobilePhotoIDDataRequest.Element])](mobilephotoiddatarequest/init(retainedelements:nonretainedelements:).md)
  Returns a photo ID data request.
- [var nonRetainedElements: [MobilePhotoIDDataRequest.Element]](mobilephotoiddatarequest/nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than necessary to process the result in realtime.
- [var retainedElements: [MobilePhotoIDDataRequest.Element]](mobilephotoiddatarequest/retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilephotoiddatarequest/element)*