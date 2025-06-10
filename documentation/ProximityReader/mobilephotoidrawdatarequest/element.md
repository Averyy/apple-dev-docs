# MobilePhotoIDRawDataRequest.Element

**Framework**: ProximityReader  
**Kind**: struct

A type representing an element that you can request from a photo ID.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Element
```

## Topics

### Operators
- [static func == (MobilePhotoIDRawDataRequest.Element, MobilePhotoIDRawDataRequest.Element) -> Bool](mobilephotoidrawdatarequest/element/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mobilephotoidrawdatarequest/element/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mobilephotoidrawdatarequest/element/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static let address: MobilePhotoIDRawDataRequest.Element](mobilephotoidrawdatarequest/element/address.md)
  The photo ID holder’s address on record with the issuer.
- [static let age: MobilePhotoIDRawDataRequest.Element](mobilephotoidrawdatarequest/element/age.md)
  The photo ID holder’s age in years.
- [static let dateOfBirth: MobilePhotoIDRawDataRequest.Element](mobilephotoidrawdatarequest/element/dateofbirth.md)
  The date of birth of the photo ID holder.
- [static let documentExpirationDate: MobilePhotoIDRawDataRequest.Element](mobilephotoidrawdatarequest/element/documentexpirationdate.md)
  The document’s expiration date.
- [static let documentIssueDate: MobilePhotoIDRawDataRequest.Element](mobilephotoidrawdatarequest/element/documentissuedate.md)
  The document’s issue date.
- [static let documentNumber: MobilePhotoIDRawDataRequest.Element](mobilephotoidrawdatarequest/element/documentnumber.md)
  The document’s number, as defined by the document’s issuing authority.
- [static let familyName: MobilePhotoIDRawDataRequest.Element](mobilephotoidrawdatarequest/element/familyname.md)
  The photo ID holder’s family name or last name.
- [static let givenName: MobilePhotoIDRawDataRequest.Element](mobilephotoidrawdatarequest/element/givenname.md)
  The photo ID holder’s given name or first name.
- [static let issuingAuthority: MobilePhotoIDRawDataRequest.Element](mobilephotoidrawdatarequest/element/issuingauthority.md)
  The state or government that issued the identity document.
- [static let portrait: MobilePhotoIDRawDataRequest.Element](mobilephotoidrawdatarequest/element/portrait.md)
  The portrait of the photo ID holder on record with the issuer.
- [static let sex: MobilePhotoIDRawDataRequest.Element](mobilephotoidrawdatarequest/element/sex.md)
  The photo ID holder’s sex.
### Type Methods
- [static func ageAtLeast(Int) -> MobilePhotoIDRawDataRequest.Element](mobilephotoidrawdatarequest/element/ageatleast(_:).md)
  A Boolean value that indicates whether the photo ID holder’s age is at least the given age.
### Default Implementations
- [Equatable Implementations](mobilephotoidrawdatarequest/element/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(retainedElements: [MobilePhotoIDRawDataRequest.Element], nonRetainedElements: [MobilePhotoIDRawDataRequest.Element])](mobilephotoidrawdatarequest/init(retainedelements:nonretainedelements:).md)
  Returns a mobile driver’s license raw data request.
- [var nonRetainedElements: [MobilePhotoIDRawDataRequest.Element]](mobilephotoidrawdatarequest/nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than is necessary to process the result in realtime.
- [var retainedElements: [MobilePhotoIDRawDataRequest.Element]](mobilephotoidrawdatarequest/retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilephotoidrawdatarequest/element)*