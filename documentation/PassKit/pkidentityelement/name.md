# name

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Type Property

The user’s full name.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- visionOS 27.0+

## Declaration

```swift
class var name: PKIdentityElement { get }
```

```objc
@property (class, nonatomic, readonly) PKIdentityElement * nameElement;
```

## Discussion

For National ID and other identity documents, requesting this element returns the person’s full name as a single properly formatted string. The response may also include [`givenName`](./givenname.md) and [`familyName`](./familyname.md) when available.

For driver’s license documents, requesting this element returns the [`givenName`](./givenname.md) and [`familyName`](./familyname.md) as separate fields, but doesn’t return a full name field. This limitation exists because the mDL (mobile Driver’s License) standard doesn’t currently include a full name field in its specification.

## See Also

### Getting identity elements
- [class var address: PKIdentityElement](./address.md)
  An element that represents the user’s home address.
- [class var dateOfBirth: PKIdentityElement](./dateofbirth.md)
  An element that represents the user’s date of birth.
- [class var dhsTemporaryLawfulStatus: PKIdentityElement](./dhstemporarylawfulstatus.md)
  Indicates whether the mobile document holder has temporary lawful status based on information from the U.S. Department of Homeland Security (DHS).
- [class var documentDHSComplianceStatus: PKIdentityElement](./documentdhscompliancestatus.md)
- [class var documentIssueDate: PKIdentityElement](./documentissuedate.md)
  An element that represents the issue date of the document.
- [class var documentExpirationDate: PKIdentityElement](./documentexpirationdate.md)
  An element that represents the expiration date of the document.
- [class var documentNumber: PKIdentityElement](./documentnumber.md)
  An element that represents the document’s number, as the issuing authority defines.
- [class var drivingPrivileges: PKIdentityElement](./drivingprivileges.md)
  An element that represents the user’s driving privileges.
- [class var eyeColor: PKIdentityElement](./eyecolor.md)
  The user’s eye color on record with the issuer.
- [class var familyName: PKIdentityElement](./familyname.md)
  An element that represents the user’s family name.
- [class var givenName: PKIdentityElement](./givenname.md)
  An element that represents the user’s given name.
- [class var hairColor: PKIdentityElement](./haircolor.md)
  The user’s hair color on record with the issuer.
- [class var height: PKIdentityElement](./height.md)
  The user’s height on record with the issuer.
- [class var issuingAuthority: PKIdentityElement](./issuingauthority.md)
  An element that represents the user’s issuing authority.
- [class var nationality: PKIdentityElement](./nationality.md)
  The mobile document holder’s nationality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityelement/name)*