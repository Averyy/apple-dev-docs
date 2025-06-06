# MobileDriversLicenseDataRequest.Response.DocumentElements

**Framework**: ProximityReader  
**Kind**: struct

A type that contains the document elements from a successful mobile driver’s license data request.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

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
### Operators
- [static func == (MobileDriversLicenseDataRequest.Response.DocumentElements, MobileDriversLicenseDataRequest.Response.DocumentElements) -> Bool](mobiledriverslicensedatarequest/response/documentelements-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
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
- [var hashValue: Int](mobiledriverslicensedatarequest/response/documentelements-swift.struct/hashvalue.md)
  The hash value.
- [let issuingAuthority: MobileDriversLicenseDataRequest.Response.DocumentElements.IssuingAuthority?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/issuingauthority-swift.property.md)
  The state or government that issued the identity document.
- [let nameComponents: PersonNameComponents?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/namecomponents.md)
  The mobile driver’s license holder’s name components.
- [let portraitData: Data?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/portraitdata.md)
  The portrait data of the mobile driver’s license holder on record with the issuer.
- [let sex: MobileDriversLicenseDataRequest.Response.DocumentElements.Sex?](mobiledriverslicensedatarequest/response/documentelements-swift.struct/sex-swift.property.md)
  The mobile driver’s license holder’s sex.
### Instance Methods
- [func hash(into: inout Hasher)](mobiledriverslicensedatarequest/response/documentelements-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Enumerations
- [MobileDriversLicenseDataRequest.Response.DocumentElements.DHSComplianceStatus](mobiledriverslicensedatarequest/response/documentelements-swift.struct/dhscompliancestatus.md)
  A type that represents the mobile driver’s license’ DHS (U.S. Department of Homeland Security) compliance status.
- [MobileDriversLicenseDataRequest.Response.DocumentElements.Sex](mobiledriverslicensedatarequest/response/documentelements-swift.struct/sex-swift.enum.md)
  A type that represents the mobile driver’s license holder’s sex.
### Default Implementations
- [Equatable Implementations](mobiledriverslicensedatarequest/response/documentelements-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedatarequest/response/documentelements-swift.struct)*