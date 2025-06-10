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
- [class var documentIssueDate: PKIdentityElement](pkidentityelement/documentissuedate.md)
  An element that represents the issue date of the document.
- [class var documentExpirationDate: PKIdentityElement](pkidentityelement/documentexpirationdate.md)
  An element that represents the expiration date of the document.
- [class var documentNumber: PKIdentityElement](pkidentityelement/documentnumber.md)
  An element that represents the document’s number, as the issuing authority defines.
- [class var drivingPrivileges: PKIdentityElement](pkidentityelement/drivingprivileges.md)
  An element that represents the user’s driving privileges.
- [class var familyName: PKIdentityElement](pkidentityelement/familyname.md)
  An element that represents the user’s family name.
- [class var givenName: PKIdentityElement](pkidentityelement/givenname.md)
  An element that represents the user’s given name.
- [class var issuingAuthority: PKIdentityElement](pkidentityelement/issuingauthority.md)
  An element that represents the user’s issuing authority.
- [class var portrait: PKIdentityElement](pkidentityelement/portrait.md)
  An element that represents the user’s photo.
### Getting an age identity element
- [class var age: PKIdentityElement](pkidentityelement/age.md)
  An element that represents the user’s age, in years.
- [class func age(atLeast: Int) -> Self](pkidentityelement/age(atleast:).md)
  Returns an element that represents the user’s age is at least the age you specify.
### Type Properties
- [class var documentDHSComplianceStatus: PKIdentityElement](pkidentityelement/documentdhscompliancestatus.md)
- [class var eyeColor: PKIdentityElement](pkidentityelement/eyecolor.md)
  The user’s eye color on record with the issuer.
- [class var hairColor: PKIdentityElement](pkidentityelement/haircolor.md)
  The user’s hair color on record with the issuer.
- [class var height: PKIdentityElement](pkidentityelement/height.md)
  The user’s height on record with the issuer.
- [class var organDonorStatus: PKIdentityElement](pkidentityelement/organdonorstatus.md)
  The user’s organ donor status on record with the issuer.
- [class var sex: PKIdentityElement](pkidentityelement/sex.md)
- [class var veteranStatus: PKIdentityElement](pkidentityelement/veteranstatus.md)
  The user’s veteran status on record with the issuer.
- [class var weight: PKIdentityElement](pkidentityelement/weight.md)
  The user’s weight on record with the issuer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md)
  Initiate a request for identity information by prompting a user for permission and decrypting a response payload.
- [Verifying Wallet identity requests](verifying-wallet-identity-requests.md)
  Decrypt and verify an in-app presentment request on your server.
- [class PKIdentityAuthorizationController](pkidentityauthorizationcontroller.md)
  An object that presents a sheet that prompts the user to allow a request for identity information.
- [class PKIdentityRequest](pkidentityrequest.md)
  An object that represents a request for identity information from a Wallet pass.
- [class PKIdentityDocument](pkidentitydocument.md)
  An object that represents the response to a request.
- [class PKIdentityButton](pkidentitybutton.md)
  An object that displays a button to trigger the identity verification flow.
- [struct VerifyIdentityWithWalletButton](verifyidentitywithwalletbutton.md)
  A view that displays a button for identity verification.
- [struct VerifyIdentityWithWalletButtonLabel](verifyidentitywithwalletbuttonlabel.md)
  A type that represents the label you use with a verify identity button.
- [struct VerifyIdentityWithWalletButtonStyle](verifyidentitywithwalletbuttonstyle.md)
  A type that represents the style you use with a verify identity button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityelement)*