# MobileNationalIDCardDataRequest.Element

**Framework**: ProximityReader  
**Kind**: struct

A type that represents an element you can request from a mobile national ID card.

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

### Type Properties
- [static let age: MobileNationalIDCardDataRequest.Element](mobilenationalidcarddatarequest/element/age.md)
  The mobile national ID card holder’s age in years.
- [static let dateOfBirth: MobileNationalIDCardDataRequest.Element](mobilenationalidcarddatarequest/element/dateofbirth.md)
  The date of birth of the mobile national ID card holder.
- [static let documentNumber: MobileNationalIDCardDataRequest.Element](mobilenationalidcarddatarequest/element/documentnumber.md)
  The document’s number, as defined by the document’s issuing authority.
- [static let familyName: MobileNationalIDCardDataRequest.Element](mobilenationalidcarddatarequest/element/familyname.md)
  The mobile national ID card holder’s family name or last name.
- [static let givenName: MobileNationalIDCardDataRequest.Element](mobilenationalidcarddatarequest/element/givenname.md)
  The mobile national ID card holder’s given name or first name.
- [static let portrait: MobileNationalIDCardDataRequest.Element](mobilenationalidcarddatarequest/element/portrait.md)
  The picture of the mobile national ID card holder on record with the issuer.
- [static let sex: MobileNationalIDCardDataRequest.Element](mobilenationalidcarddatarequest/element/sex.md)
  The mobile national ID card holder’s sex.
### Type Methods
- [static func ageAtLeast(Int) -> MobileNationalIDCardDataRequest.Element](mobilenationalidcarddatarequest/element/ageatleast(_:).md)
  A Boolean value that indicates whether the mobile national ID card holder’s age is at least the given age.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var region: Locale.Region](mobilenationalidcarddatarequest/region.md)
  The region of the document you’re requesting.
- [var retainedElements: [MobileNationalIDCardDataRequest.Element]](mobilenationalidcarddatarequest/retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.
- [var nonRetainedElements: [MobileNationalIDCardDataRequest.Element]](mobilenationalidcarddatarequest/nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than necessary to process the result in realtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilenationalidcarddatarequest/element)*