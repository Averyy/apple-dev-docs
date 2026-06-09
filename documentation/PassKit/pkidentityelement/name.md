# name

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The user’s full name.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class var name: PKIdentityElement { get }
```

#### Discussion

For National ID and other identity documents, requesting this element returns the person’s full name as a single properly formatted string. The response may also include [`givenName`](pkidentityelement/givenname.md) and [`familyName`](pkidentityelement/familyname.md) when available.

For driver’s license documents, requesting this element returns the [`givenName`](pkidentityelement/givenname.md) and [`familyName`](pkidentityelement/familyname.md) as separate fields, but doesn’t return a full name field. This limitation exists because the mDL (mobile Driver’s License) standard doesn’t currently include a full name field in its specification.

## See Also

- [class var address: PKIdentityElement](pkidentityelement/address.md)
  An element that represents the user’s home address.
- [class var dateOfBirth: PKIdentityElement](pkidentityelement/dateofbirth.md)
  An element that represents the user’s date of birth.
- [class var dhsTemporaryLawfulStatus: PKIdentityElement](pkidentityelement/dhstemporarylawfulstatus.md)
  Indicates whether the mobile document holder has temporary lawful status based on information from the U.S. Department of Homeland Security (DHS).
- [class var documentDHSComplianceStatus: PKIdentityElement](pkidentityelement/documentdhscompliancestatus.md)
- [class var documentIssueDate: PKIdentityElement](pkidentityelement/documentissuedate.md)
  An element that represents the issue date of the document.
- [class var documentExpirationDate: PKIdentityElement](pkidentityelement/documentexpirationdate.md)
  An element that represents the expiration date of the document.
- [class var documentNumber: PKIdentityElement](pkidentityelement/documentnumber.md)
  An element that represents the document’s number, as the issuing authority defines.
- [class var drivingPrivileges: PKIdentityElement](pkidentityelement/drivingprivileges.md)
  An element that represents the user’s driving privileges.
- [class var eyeColor: PKIdentityElement](pkidentityelement/eyecolor.md)
  The user’s eye color on record with the issuer.
- [class var familyName: PKIdentityElement](pkidentityelement/familyname.md)
  An element that represents the user’s family name.
- [class var givenName: PKIdentityElement](pkidentityelement/givenname.md)
  An element that represents the user’s given name.
- [class var hairColor: PKIdentityElement](pkidentityelement/haircolor.md)
  The user’s hair color on record with the issuer.
- [class var height: PKIdentityElement](pkidentityelement/height.md)
  The user’s height on record with the issuer.
- [class var issuingAuthority: PKIdentityElement](pkidentityelement/issuingauthority.md)
  An element that represents the user’s issuing authority.
- [class var nationality: PKIdentityElement](pkidentityelement/nationality.md)
  The mobile document holder’s nationality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityelement/name)*