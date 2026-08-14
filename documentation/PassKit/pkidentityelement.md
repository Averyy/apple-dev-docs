# PKIdentityElement

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that represents the elements an app requests from identity documents.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class PKIdentityElement
```

#### Overview

If an app requests an element from a document type that doesn’t support it, the system ignores the element.

## Topics

### Getting identity elements
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
- [class var name: PKIdentityElement](pkidentityelement/name.md)
  The user’s full name.
- [class var nationality: PKIdentityElement](pkidentityelement/nationality.md)
  The mobile document holder’s nationality.
- [class var organDonorStatus: PKIdentityElement](pkidentityelement/organdonorstatus.md)
  The user’s organ donor status on record with the issuer.
- [class var placeOfBirth: PKIdentityElement](pkidentityelement/placeofbirth.md)
  The place where the mobile document holder was born.
- [class var portrait: PKIdentityElement](pkidentityelement/portrait.md)
  An element that represents the user’s photo.
- [class var sex: PKIdentityElement](pkidentityelement/sex.md)
  An element that represents the document holder’s sex.
- [class var signatureUsualMark: PKIdentityElement](pkidentityelement/signatureusualmark.md)
  The signature or usual mark of the mobile document holder.
- [class var weight: PKIdentityElement](pkidentityelement/weight.md)
  The user’s weight on record with the issuer.
- [class var veteranStatus: PKIdentityElement](pkidentityelement/veteranstatus.md)
  The user’s veteran status on record with the issuer.
- [class var signatureUsualMark: PKIdentityElement](pkidentityelement/signatureusualmark.md)
  The signature or usual mark of the mobile document holder.
- [class var placeOfBirth: PKIdentityElement](pkidentityelement/placeofbirth.md)
  The place where the mobile document holder was born.
- [class var nationality: PKIdentityElement](pkidentityelement/nationality.md)
  The mobile document holder’s nationality.
- [class var dhsTemporaryLawfulStatus: PKIdentityElement](pkidentityelement/dhstemporarylawfulstatus.md)
  Indicates whether the mobile document holder has temporary lawful status based on information from the U.S. Department of Homeland Security (DHS).
### Getting an age identity element
- [class var age: PKIdentityElement](pkidentityelement/age.md)
  An element that represents the user’s age, in years.
- [class func age(atLeast: Int) -> Self](pkidentityelement/age(atleast:).md)
  Returns an element that represents the user’s age is at least the age you specify.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class PKIdentityAuthorizationController](pkidentityauthorizationcontroller.md)
  An object that presents a sheet that prompts the user to allow a request for identity information.
- [class PKIdentityRequest](pkidentityrequest.md)
  An object that represents a request for identity information from a Wallet pass.
- [class PKIdentityDocument](pkidentitydocument.md)
  An object that represents the response to a request.
- [class PKIdentityButton](pkidentitybutton.md)
  An object that displays a button to trigger the identity verification flow.
- [struct VerifyIdentityWithWalletButton](verifyidentitywithwalletbutton.md)
  A type that displays a button to present the identity verification flow.
- [struct VerifyIdentityWithWalletButtonLabel](verifyidentitywithwalletbuttonlabel.md)
  A type that represents the label you use with a verify identity button.
- [struct VerifyIdentityWithWalletButtonStyle](verifyidentitywithwalletbuttonstyle.md)
  A type that represents the style you use with a verify identity button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityelement)*