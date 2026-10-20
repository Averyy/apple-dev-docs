# MobileDriversLicenseRawDataRequest.Element

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

A type representing an element that you can request from a mobile driver’s license.

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
- [static let address: MobileDriversLicenseRawDataRequest.Element](./element/address.md)
  The mobile driver’s license holder’s address on record with the issuer.
- [static let age: MobileDriversLicenseRawDataRequest.Element](./element/age.md)
  The mobile driver’s license holder’s age in years.
- [static let dateOfBirth: MobileDriversLicenseRawDataRequest.Element](./element/dateofbirth.md)
  The date of birth of the mobile driver’s license holder.
- [static let dhsTemporaryLawfulStatus: MobileDriversLicenseRawDataRequest.Element](./element/dhstemporarylawfulstatus.md)
  Indicates whether the mobile document holder has temporary lawful status based on information from the U.S. Department of Homeland Security (DHS).
- [static let documentDHSComplianceStatus: MobileDriversLicenseRawDataRequest.Element](./element/documentdhscompliancestatus.md)
  The document’s DHS (U.S. Department of Homeland Security) compliance status.
- [static let documentExpirationDate: MobileDriversLicenseRawDataRequest.Element](./element/documentexpirationdate.md)
  The document’s expiration date.
- [static let documentIssueDate: MobileDriversLicenseRawDataRequest.Element](./element/documentissuedate.md)
  The document’s issue date.
- [static let documentNumber: MobileDriversLicenseRawDataRequest.Element](./element/documentnumber.md)
  The document’s number, as defined by the document’s issuing authority.
- [static let drivingPrivileges: MobileDriversLicenseRawDataRequest.Element](./element/drivingprivileges.md)
  The mobile driver’s license holder’s driving privileges.
- [static let eyeColor: MobileDriversLicenseRawDataRequest.Element](./element/eyecolor.md)
  The mobile driver’s license holder’s eye color on record with the issuer.
- [static let familyName: MobileDriversLicenseRawDataRequest.Element](./element/familyname.md)
  The mobile driver’s license holder’s family name or last name.
- [static let givenName: MobileDriversLicenseRawDataRequest.Element](./element/givenname.md)
  The mobile driver’s license holder’s given name or first name.
- [static let hairColor: MobileDriversLicenseRawDataRequest.Element](./element/haircolor.md)
  The mobile driver’s license holder’s hair color on record with the issuer.
- [static let height: MobileDriversLicenseRawDataRequest.Element](./element/height.md)
  The mobile driver’s license holder’s height on record with the issuer.
- [static let issuingAuthority: MobileDriversLicenseRawDataRequest.Element](./element/issuingauthority.md)
  The state or government that issued the identity document.
- [static let name: MobileDriversLicenseRawDataRequest.Element](./element/name.md)
  The mobile driver’s license holder’s name.
- [static let nationality: MobileDriversLicenseRawDataRequest.Element](./element/nationality.md)
  The mobile document holder’s nationality.
- [static let organDonorStatus: MobileDriversLicenseRawDataRequest.Element](./element/organdonorstatus.md)
  The mobile driver’s license holder’s organ donor status on record with the issuer.
- [static let placeOfBirth: MobileDriversLicenseRawDataRequest.Element](./element/placeofbirth.md)
  The place where the mobile document holder was born.
- [static let portrait: MobileDriversLicenseRawDataRequest.Element](./element/portrait.md)
  The portrait of the mobile driver’s license holder on record with the issuer.
- [static let sex: MobileDriversLicenseRawDataRequest.Element](./element/sex.md)
  The mobile driver’s license holder’s sex.
- [static let signatureUsualMark: MobileDriversLicenseRawDataRequest.Element](./element/signatureusualmark.md)
  The signature or usual mark of the mobile document holder.
- [static let veteranStatus: MobileDriversLicenseRawDataRequest.Element](./element/veteranstatus.md)
  The mobile driver’s license holder’s veteran status on record with the issuer.
- [static let weight: MobileDriversLicenseRawDataRequest.Element](./element/weight.md)
  The mobile driver’s license holder’s weight on record with the issuer.
### Type Methods
- [static func ageAtLeast(Int) -> MobileDriversLicenseRawDataRequest.Element](./element/ageatleast%28_%29.md)
  A Boolean value that indicates whether the mobile driver’s license holder’s age is at least the given age.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a raw data request
- [init(retainedElements: [MobileDriversLicenseRawDataRequest.Element], nonRetainedElements: [MobileDriversLicenseRawDataRequest.Element])](./init%28retainedelements,nonretainedelements%29.md)
  Returns a mobile driver’s license raw data request.
- [var retainedElements: [MobileDriversLicenseRawDataRequest.Element]](./retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.
- [var nonRetainedElements: [MobileDriversLicenseRawDataRequest.Element]](./nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than is necessary to process the result in realtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicenserawdatarequest/element)*