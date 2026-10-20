# MobileNationalIDCardRawDataRequest.Element

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

A type representing an element that you can request from a mobile national ID card.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
struct Element
```

## Topics

### Type Properties
- [static let address: MobileNationalIDCardRawDataRequest.Element](./element/address.md)
  The mobile national ID card holder’s address on record with the issuer.
- [static let age: MobileNationalIDCardRawDataRequest.Element](./element/age.md)
  The mobile national ID card holder’s age in years.
- [static let dateOfBirth: MobileNationalIDCardRawDataRequest.Element](./element/dateofbirth.md)
  The date of birth of the mobile national ID card holder.
- [static let documentNumber: MobileNationalIDCardRawDataRequest.Element](./element/documentnumber.md)
  The document’s number, as defined by the document’s issuing authority.
- [static let familyName: MobileNationalIDCardRawDataRequest.Element](./element/familyname.md)
  The mobile national ID card holder’s family name or last name.
- [static let givenName: MobileNationalIDCardRawDataRequest.Element](./element/givenname.md)
  The mobile national ID card holder’s given name or first name.
- [static let name: MobileNationalIDCardRawDataRequest.Element](./element/name.md)
  The mobile national ID card holder’s name.
- [static let portrait: MobileNationalIDCardRawDataRequest.Element](./element/portrait.md)
  The portrait of the mobile national ID card holder on record with the issuer.
- [static let sex: MobileNationalIDCardRawDataRequest.Element](./element/sex.md)
  The mobile national ID card holder’s sex.
### Type Methods
- [static func ageAtLeast(Int) -> MobileNationalIDCardRawDataRequest.Element](./element/ageatleast%28_%29.md)
  A Boolean value that indicates whether the mobile national ID card holder’s age is at least the given age.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the request details
- [var region: Locale.Region](./region.md)
  The region of the document you’re requesting.
- [var retainedElements: [MobileNationalIDCardRawDataRequest.Element]](./retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.
- [var nonRetainedElements: [MobileNationalIDCardRawDataRequest.Element]](./nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than is necessary to process the result in realtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilenationalidcardrawdatarequest/element)*