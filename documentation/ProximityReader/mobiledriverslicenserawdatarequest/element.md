# MobileDriversLicenseRawDataRequest.Element

**Framework**: ProximityReader  
**Kind**: struct

A type representing an element that you can request from a mobile driver’s license.

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

### Operators
- [static func == (MobileDriversLicenseRawDataRequest.Element, MobileDriversLicenseRawDataRequest.Element) -> Bool](mobiledriverslicenserawdatarequest/element/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mobiledriverslicenserawdatarequest/element/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mobiledriverslicenserawdatarequest/element/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static let address: MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element/address.md)
  The mobile driver’s license holder’s address on record with the issuer.
- [static let age: MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element/age.md)
  The mobile driver’s license holder’s age in years.
- [static let dateOfBirth: MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element/dateofbirth.md)
  The date of birth of the mobile driver’s license holder.
- [static let documentDHSComplianceStatus: MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element/documentdhscompliancestatus.md)
  The document’s DHS (U.S. Department of Homeland Security) compliance status.
- [static let documentExpirationDate: MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element/documentexpirationdate.md)
  The document’s expiration date.
- [static let documentIssueDate: MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element/documentissuedate.md)
  The document’s issue date.
- [static let documentNumber: MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element/documentnumber.md)
  The document’s number, as defined by the document’s issuing authority.
- [static let drivingPrivileges: MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element/drivingprivileges.md)
  The mobile driver’s license holder’s driving privileges.
- [static let eyeColor: MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element/eyecolor.md)
  The mobile driver’s license holder’s eye color on record with the issuer.
- [static let familyName: MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element/familyname.md)
  The mobile driver’s license holder’s family name or last name.
- [static let givenName: MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element/givenname.md)
  The mobile driver’s license holder’s given name or first name.
- [static let hairColor: MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element/haircolor.md)
  The mobile driver’s license holder’s hair color on record with the issuer.
- [static let height: MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element/height.md)
  The mobile driver’s license holder’s height on record with the issuer.
- [static let issuingAuthority: MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element/issuingauthority.md)
  The state or government that issued the identity document.
- [static let organDonorStatus: MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element/organdonorstatus.md)
  The mobile driver’s license holder’s organ donor status on record with the issuer.
- [static let portrait: MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element/portrait.md)
  The portrait of the mobile driver’s license holder on record with the issuer.
- [static let sex: MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element/sex.md)
  The mobile driver’s license holder’s sex.
- [static let veteranStatus: MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element/veteranstatus.md)
  The mobile driver’s license holder’s veteran status on record with the issuer.
- [static let weight: MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element/weight.md)
  The mobile driver’s license holder’s weight on record with the issuer.
### Type Methods
- [static func ageAtLeast(Int) -> MobileDriversLicenseRawDataRequest.Element](mobiledriverslicenserawdatarequest/element/ageatleast(_:).md)
  A Boolean value that indicates whether the mobile driver’s license holder’s age is at least the given age.
### Default Implementations
- [Equatable Implementations](mobiledriverslicenserawdatarequest/element/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(retainedElements: [MobileDriversLicenseRawDataRequest.Element], nonRetainedElements: [MobileDriversLicenseRawDataRequest.Element])](mobiledriverslicenserawdatarequest/init(retainedelements:nonretainedelements:).md)
  Returns a mobile driver’s license raw data request.
- [var retainedElements: [MobileDriversLicenseRawDataRequest.Element]](mobiledriverslicenserawdatarequest/retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.
- [var nonRetainedElements: [MobileDriversLicenseRawDataRequest.Element]](mobiledriverslicenserawdatarequest/nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than is necessary to process the result in realtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicenserawdatarequest/element)*