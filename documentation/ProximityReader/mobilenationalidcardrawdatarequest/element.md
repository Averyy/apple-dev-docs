# MobileNationalIDCardRawDataRequest.Element

**Framework**: ProximityReader  
**Kind**: struct

A type representing an element that you can request from a mobile national ID card.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
struct Element
```

## Topics

### Operators
- [static func == (MobileNationalIDCardRawDataRequest.Element, MobileNationalIDCardRawDataRequest.Element) -> Bool](mobilenationalidcardrawdatarequest/element/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mobilenationalidcardrawdatarequest/element/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mobilenationalidcardrawdatarequest/element/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static let address: MobileNationalIDCardRawDataRequest.Element](mobilenationalidcardrawdatarequest/element/address.md)
  The mobile national ID card holder’s address on record with the issuer.
- [static let age: MobileNationalIDCardRawDataRequest.Element](mobilenationalidcardrawdatarequest/element/age.md)
  The mobile national ID card holder’s age in years.
- [static let dateOfBirth: MobileNationalIDCardRawDataRequest.Element](mobilenationalidcardrawdatarequest/element/dateofbirth.md)
  The date of birth of the mobile national ID card holder.
- [static let documentNumber: MobileNationalIDCardRawDataRequest.Element](mobilenationalidcardrawdatarequest/element/documentnumber.md)
  The document’s number, as defined by the document’s issuing authority.
- [static let familyName: MobileNationalIDCardRawDataRequest.Element](mobilenationalidcardrawdatarequest/element/familyname.md)
  The mobile national ID card holder’s family name or last name.
- [static let givenName: MobileNationalIDCardRawDataRequest.Element](mobilenationalidcardrawdatarequest/element/givenname.md)
  The mobile national ID card holder’s given name or first name.
- [static let portrait: MobileNationalIDCardRawDataRequest.Element](mobilenationalidcardrawdatarequest/element/portrait.md)
  The portrait of the mobile national ID card holder on record with the issuer.
- [static let sex: MobileNationalIDCardRawDataRequest.Element](mobilenationalidcardrawdatarequest/element/sex.md)
  The mobile national ID card holder’s sex.
### Type Methods
- [static func ageAtLeast(Int) -> MobileNationalIDCardRawDataRequest.Element](mobilenationalidcardrawdatarequest/element/ageatleast(_:).md)
  A Boolean value that indicates whether the mobile national ID card holder’s age is at least the given age.
### Default Implementations
- [Equatable Implementations](mobilenationalidcardrawdatarequest/element/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var region: Locale.Region](mobilenationalidcardrawdatarequest/region.md)
  The region of the document you’re requesting.
- [var retainedElements: [MobileNationalIDCardRawDataRequest.Element]](mobilenationalidcardrawdatarequest/retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.
- [var nonRetainedElements: [MobileNationalIDCardRawDataRequest.Element]](mobilenationalidcardrawdatarequest/nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than is necessary to process the result in realtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilenationalidcardrawdatarequest/element)*