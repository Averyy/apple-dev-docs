# JPKIPassContents.SigningIdentity

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

The authentication for signing user identification.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
struct SigningIdentity
```

#### Overview

Use this structure to define valid signature identity authentication.

## Topics

### Signing identity authentication
- [let signingIdentity: JPKIPassContents.SigningIdentity?](jpkipasscontents/signingidentity-swift.property.md)
  Allows access to the signing identity, if present in the JPKI applet.
- [func changePassword(from: String, to: String) async throws](jpkipasscontents/signingidentity-swift.struct/changepassword(from:to:).md)
  A function that allows you to change the password associated with the signing identity.
- [JPKIPassContents.SigningIdentity.AuthenticationType](jpkipasscontents/signingidentity-swift.struct/authenticationtype.md)
  Defines the valid user authentication request options for the signing identity.

## Relationships

### Conforms To
- [JPKIPassContents.Identity](jpkipasscontents/identity.md)

## See Also

- [JPKIPassContents.UserIdentity](jpkipasscontents/useridentity-swift.struct.md)
  The functionality for the type of user identification.
- [JPKIPassContents.Signature](jpkipasscontents/signature.md)
  The resulting signed data and certificate you use to sign the pass.
- [JPKIPassContents.Certificate](jpkipasscontents/certificate.md)
  The certificate data associated with an identity document.
- [JPKIPassContents.AuthenticationRequest](jpkipasscontents/authenticationrequest.md)
  The user authentification request based on the generics type.
- [JPKIPassContents.Identity](jpkipasscontents/identity.md)
  Defines the common functionality that JPKI digital identities support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/signingidentity-swift.struct)*