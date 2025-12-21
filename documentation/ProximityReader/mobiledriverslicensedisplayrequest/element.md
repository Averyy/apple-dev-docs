# MobileDriversLicenseDisplayRequest.Element

**Framework**: ProximityReader  
**Kind**: struct

A type that represents an element you can request from a mobile driver’s license.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
struct Element
```

## Topics

### Type Properties
- [static let age: MobileDriversLicenseDisplayRequest.Element](mobiledriverslicensedisplayrequest/element/age.md)
  The mobile driver’s license holder’s age in years.
- [static let familyName: MobileDriversLicenseDisplayRequest.Element](mobiledriverslicensedisplayrequest/element/familyname.md)
  The mobile driver’s license holder’s family name or last name.
- [static let givenName: MobileDriversLicenseDisplayRequest.Element](mobiledriverslicensedisplayrequest/element/givenname.md)
  The mobile driver’s license holder’s given name or first name.
### Type Methods
- [static func ageAtLeast(Int) -> MobileDriversLicenseDisplayRequest.Element](mobiledriverslicensedisplayrequest/element/ageatleast(_:).md)
  A Boolean value that indicates whether the mobile driver’s license holder’s age is at least the given age.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(elements: [MobileDriversLicenseDisplayRequest.Element], options: MobileDriversLicenseDisplayRequest.Options)](mobiledriverslicensedisplayrequest/init(elements:options:).md)
  Creates a new mobile driver’s license display request.
- [var elements: [MobileDriversLicenseDisplayRequest.Element]](mobiledriverslicensedisplayrequest/elements.md)
  The document elements you’re requesting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedisplayrequest/element)*