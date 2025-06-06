# MobileDriversLicenseDataRequest.Element

**Framework**: ProximityReader  
**Kind**: struct

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

### Operators
- [static func == (MobileDriversLicenseDataRequest.Element, MobileDriversLicenseDataRequest.Element) -> Bool](mobiledriverslicensedatarequest/element/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mobiledriverslicensedatarequest/element/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mobiledriverslicensedatarequest/element/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static let address: MobileDriversLicenseDataRequest.Element](mobiledriverslicensedatarequest/element/address.md)
  The mobile driver’s license holder’s address on record with the issuer.
- [static let age: MobileDriversLicenseDataRequest.Element](mobiledriverslicensedatarequest/element/age.md)
  The mobile driver’s license holder’s age in years.
- [static let dateOfBirth: MobileDriversLicenseDataRequest.Element](mobiledriverslicensedatarequest/element/dateofbirth.md)
  The date of birth of the mobile driver’s license holder.
- [static let documentDHSComplianceStatus: MobileDriversLicenseDataRequest.Element](mobiledriverslicensedatarequest/element/documentdhscompliancestatus.md)
  The document’s DHS (U.S. Department of Homeland Security) compliance status.
- [static let documentExpirationDate: MobileDriversLicenseDataRequest.Element](mobiledriverslicensedatarequest/element/documentexpirationdate.md)
  The document’s expiration date.
- [static let documentIssueDate: MobileDriversLicenseDataRequest.Element](mobiledriverslicensedatarequest/element/documentissuedate.md)
  The document’s issue date.
- [static let documentNumber: MobileDriversLicenseDataRequest.Element](mobiledriverslicensedatarequest/element/documentnumber.md)
  The document’s number, as defined by the document’s issuing authority.
- [static let drivingPrivileges: MobileDriversLicenseDataRequest.Element](mobiledriverslicensedatarequest/element/drivingprivileges.md)
  The mobile driver’s license holder’s driving privileges.
- [static let familyName: MobileDriversLicenseDataRequest.Element](mobiledriverslicensedatarequest/element/familyname.md)
  The mobile driver’s license holder’s family name or last name.
- [static let givenName: MobileDriversLicenseDataRequest.Element](mobiledriverslicensedatarequest/element/givenname.md)
  The mobile driver’s license holder’s given name or first name.
- [static let issuingAuthority: MobileDriversLicenseDataRequest.Element](mobiledriverslicensedatarequest/element/issuingauthority.md)
  The state or government that issued the identity document.
- [static let portrait: MobileDriversLicenseDataRequest.Element](mobiledriverslicensedatarequest/element/portrait.md)
  The picture of the mobile driver’s license holder on record with the issuer.
- [static let sex: MobileDriversLicenseDataRequest.Element](mobiledriverslicensedatarequest/element/sex.md)
  The mobile driver’s license holder’s sex.
### Type Methods
- [static func ageAtLeast(Int) -> MobileDriversLicenseDataRequest.Element](mobiledriverslicensedatarequest/element/ageatleast(_:).md)
  A Boolean value that indicates whether the mobile driver’s license holder’s age is at least the given age.
### Default Implementations
- [Equatable Implementations](mobiledriverslicensedatarequest/element/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(retainedElements: [MobileDriversLicenseDataRequest.Element], nonRetainedElements: [MobileDriversLicenseDataRequest.Element])](mobiledriverslicensedatarequest/init(retainedelements:nonretainedelements:).md)
  Returns a mobile driver’s license data request.
- [var retainedElements: [MobileDriversLicenseDataRequest.Element]](mobiledriverslicensedatarequest/retainedelements.md)
  The document elements you’re requesting and intend to retain for an indefinite period of time.
- [var nonRetainedElements: [MobileDriversLicenseDataRequest.Element]](mobiledriverslicensedatarequest/nonretainedelements.md)
  The document elements you’re requesting and intend to retain no longer than necessary to process the result in realtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedatarequest/element)*