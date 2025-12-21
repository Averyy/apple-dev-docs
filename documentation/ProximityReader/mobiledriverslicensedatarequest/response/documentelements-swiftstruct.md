# MobileDriversLicenseDataRequest.Response.DocumentElements

**Framework**: ProximityReader  
**Kind**: struct

A type that contains the document elements from a successful mobile driver’s license data request.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
struct DocumentElements
```

## Topics

### Structures
- [MobileDriversLicenseDataRequest.Response.DocumentElements.AAMVADrivingPrivilege](mobiledriverslicensedatarequest/response/documentelements-swift.struct/aamvadrivingprivilege.md)
  A type that represents the mobile driver’s license holder’s AAMVA driving privileges.
- [MobileDriversLicenseDataRequest.Response.DocumentElements.DrivingPrivilege](mobiledriverslicensedatarequest/response/documentelements-swift.struct/drivingprivilege.md)
  A type that represents a driving privilege which the mobile driver’s license holder possesses.
- [MobileDriversLicenseDataRequest.Response.DocumentElements.IssuingAuthority](mobiledriverslicensedatarequest/response/documentelements-swift.struct/issuingauthority-swift.struct.md)
  A type that represents the state or government that issued the identity document.
### Instance Properties
- [let aamvaDrivingPrivileges: [MobileDriversLicenseDataRequest.Response.DocumentElements.AAMVADrivingPrivilege]](mobiledriverslicensedatarequest/response/documentelements-swift.struct/aamvadrivingprivileges.md)
  The mobile driver’s license holder’s AAMVA driving privileges.
- [var address: CNPostalAddress?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/address.md)
  The mobile driver’s license holder’s address on record with the issuer.
- [let age: Int?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/age.md)
  The mobile driver’s license holder’s age in years.
- [let ageAtLeastElements: [Int : Bool]](mobiledriverslicensedatarequest/response/documentelements-swift.struct/ageatleastelements.md)
  A dictionary of values that indicate whether the document holder is at least the specified age.
- [let dateOfBirth: DateComponents?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/dateofbirth.md)
  The date of birth of the mobile driver’s license holder.
- [let documentDHSComplianceStatus: MobileDriversLicenseDataRequest.Response.DocumentElements.DHSComplianceStatus?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/documentdhscompliancestatus.md)
  The document’s DHS (U.S. Department of Homeland Security) compliance status.
- [let documentExpirationDate: DateComponents?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/documentexpirationdate.md)
  The document’s expiration date.
- [let documentIssueDate: DateComponents?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/documentissuedate.md)
  The document’s issue date.
- [let documentNumber: String?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/documentnumber.md)
  The document’s number, as defined by the document’s issuing authority.
- [let drivingPrivileges: [MobileDriversLicenseDataRequest.Response.DocumentElements.DrivingPrivilege]](mobiledriverslicensedatarequest/response/documentelements-swift.struct/drivingprivileges.md)
  The mobile driver’s license holder’s driving privileges.
- [let eyeColor: MobileDriversLicenseDataRequest.Response.DocumentElements.EyeColor?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/eyecolor-swift.property.md)
  The mobile identity document holder’s eye color on record with the issuer.
- [let hairColor: MobileDriversLicenseDataRequest.Response.DocumentElements.HairColor?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/haircolor-swift.property.md)
  The mobile identity document holder’s hair color on record with the issuer.
- [let height: Measurement<UnitLength>?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/height.md)
  The mobile identity document holder’s height on record with the issuer.
- [let isOrganDonor: Bool?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/isorgandonor.md)
  A Boolean value indicating whether the identity document holder is an organ donor.
- [let isVeteran: Bool?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/isveteran.md)
  A Boolean value indicating whether the identity document holder is a veteran.
- [let issuingAuthority: MobileDriversLicenseDataRequest.Response.DocumentElements.IssuingAuthority?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/issuingauthority-swift.property.md)
  The state or government that issued the identity document.
- [let nameComponents: PersonNameComponents?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/namecomponents.md)
  The mobile driver’s license holder’s name components.
- [let portraitData: Data?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/portraitdata.md)
  The portrait data of the mobile driver’s license holder on record with the issuer.
- [let sex: MobileDriversLicenseDataRequest.Response.DocumentElements.Sex?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/sex-swift.property.md)
  The mobile driver’s license holder’s sex.
- [let weight: Measurement<UnitMass>?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/weight.md)
  The mobile identity document holder’s weight on record with the issuer.
### Enumerations
- [MobileDriversLicenseDataRequest.Response.DocumentElements.DHSComplianceStatus](mobiledriverslicensedatarequest/response/documentelements-swift.struct/dhscompliancestatus.md)
  A type that represents the mobile driver’s license’ DHS (U.S. Department of Homeland Security) compliance status.
- [MobileDriversLicenseDataRequest.Response.DocumentElements.EyeColor](mobiledriverslicensedatarequest/response/documentelements-swift.struct/eyecolor-swift.enum.md)
  A type that represents the mobile driver’s license holder’s eye color
- [MobileDriversLicenseDataRequest.Response.DocumentElements.HairColor](mobiledriverslicensedatarequest/response/documentelements-swift.struct/haircolor-swift.enum.md)
  A type that represents the mobile driver’s license holder’s hair color
- [MobileDriversLicenseDataRequest.Response.DocumentElements.Sex](mobiledriverslicensedatarequest/response/documentelements-swift.struct/sex-swift.enum.md)
  A type that represents the mobile driver’s license holder’s sex.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedatarequest/response/documentelements-swift.struct)*