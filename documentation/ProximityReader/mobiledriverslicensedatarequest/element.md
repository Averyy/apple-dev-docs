# MobileDriversLicenseDataRequest.Element

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
- [static let address: MobileDriversLicenseDataRequest.Element](./element/address.md)
  The mobile driver’s license holder’s address on record with the issuer.
- [static let age: MobileDriversLicenseDataRequest.Element](./element/age.md)
  The mobile driver’s license holder’s age in years.
- [static let dateOfBirth: MobileDriversLicenseDataRequest.Element](./element/dateofbirth.md)
  The date of birth of the mobile driver’s license holder.
- [static let documentDHSComplianceStatus: MobileDriversLicenseDataRequest.Element](./element/documentdhscompliancestatus.md)
  The document’s DHS (U.S. Department of Homeland Security) compliance status.
- [static let documentExpirationDate: MobileDriversLicenseDataRequest.Element](./element/documentexpirationdate.md)
  The document’s expiration date.
- [static let documentIssueDate: MobileDriversLicenseDataRequest.Element](./element/documentissuedate.md)
  The document’s issue date.
- [static let documentNumber: MobileDriversLicenseDataRequest.Element](./element/documentnumber.md)
  The document’s number, as defined by the document’s issuing authority.
- [static let drivingPrivileges: MobileDriversLicenseDataRequest.Element](./element/drivingprivileges.md)
  The mobile driver’s license holder’s driving privileges.
- [static let eyeColor: MobileDriversLicenseDataRequest.Element](./element/eyecolor.md)
  The mobile driver’s license holder’s eye color on record with the issuer.
- [static let familyName: MobileDriversLicenseDataRequest.Element](./element/familyname.md)
  The mobile driver’s license holder’s family name or last name.
- [static let givenName: MobileDriversLicenseDataRequest.Element](./element/givenname.md)
  The mobile driver’s license holder’s given name or first name.
- [static let hairColor: MobileDriversLicenseDataRequest.Element](./element/haircolor.md)
  The mobile driver’s license holder’s hair color on record with the issuer.
- [static let height: MobileDriversLicenseDataRequest.Element](./element/height.md)
  The mobile driver’s license holder’s height on record with the issuer.
- [static let issuingAuthority: MobileDriversLicenseDataRequest.Element](./element/issuingauthority.md)
  The state or government that issued the identity document.
- [static let name: MobileDriversLicenseDataRequest.Element](./element/name.md)
  The mobile driver’s license holder’s name.
- [static let nationality: MobileDriversLicenseDataRequest.Element](./element/nationality.md)
  The mobile driver’s license holder’s nationality on record with the issuer.
- [static let organDonorStatus: MobileDriversLicenseDataRequest.Element](./element/organdonorstatus.md)
  The mobile driver’s license holder’s organ donor status on record with the issuer.
- [static let placeOfBirth: MobileDriversLicenseDataRequest.Element](./element/placeofbirth.md)
  The mobile driver’s license holder’s birth place on record with the issuer.
- [static let portrait: MobileDriversLicenseDataRequest.Element](./element/portrait.md)
  The picture of the mobile driver’s license holder on record with the issuer.
- [static let sex: MobileDriversLicenseDataRequest.Element](./element/sex.md)
  The mobile driver’s license holder’s sex.
- [static let signatureUsualMark: MobileDriversLicenseDataRequest.Element](./element/signatureusualmark.md)
  The mobile driver’s license holder’s signature or usual mark on record with the issuer.
- [static let veteranStatus: MobileDriversLicenseDataRequest.Element](./element/veteranstatus.md)
  The mobile driver’s license holder’s veteran status on record with the issuer.
- [static let weight: MobileDriversLicenseDataRequest.Element](./element/weight.md)
  The mobile driver’s license holder’s weight on record with the issuer.
### Type Methods
- [static func ageAtLeast(Int) -> MobileDriversLicenseDataRequest.Element](./element/ageatleast%28_%29.md)
  A Boolean value that indicates whether the mobile driver’s license holder’s age is at least the given age.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a data request
- [init(retainedElements: [MobileDriversLicenseDataRequest.Element], nonRetainedElements: [MobileDriversLicenseDataRequest.Element])](./init%28retainedelements,nonretainedelements%29.md)
  Returns a mobile driver’s license data request.
- [var retainedElements: [MobileDriversLicenseDataRequest.Element]](./retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.
- [var nonRetainedElements: [MobileDriversLicenseDataRequest.Element]](./nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than necessary to process the result in realtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedatarequest/element)*