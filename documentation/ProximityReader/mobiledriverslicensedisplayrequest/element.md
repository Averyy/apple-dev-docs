# MobileDriversLicenseDisplayRequest.Element

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

A type that represents an element you can request from a mobile driver’s license.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
struct Element
```

## Topics

### Type Properties
- [static let age: MobileDriversLicenseDisplayRequest.Element](./element/age.md)
  The mobile driver’s license holder’s age in years.
- [static let familyName: MobileDriversLicenseDisplayRequest.Element](./element/familyname.md)
  The mobile driver’s license holder’s family name or last name.
- [static let givenName: MobileDriversLicenseDisplayRequest.Element](./element/givenname.md)
  The mobile driver’s license holder’s given name or first name.
- [static let name: MobileDriversLicenseDisplayRequest.Element](./element/name.md)
  The mobile driver’s license holder’s name.
### Type Methods
- [static func ageAtLeast(Int) -> MobileDriversLicenseDisplayRequest.Element](./element/ageatleast%28_%29.md)
  A Boolean value that indicates whether the mobile driver’s license holder’s age is at least the given age.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a display request
- [init(elements: [MobileDriversLicenseDisplayRequest.Element], options: MobileDriversLicenseDisplayRequest.Options)](./init%28elements,options%29.md)
  Creates a new mobile driver’s license display request.
- [var elements: [MobileDriversLicenseDisplayRequest.Element]](./elements.md)
  The document elements you’re requesting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedisplayrequest/element)*