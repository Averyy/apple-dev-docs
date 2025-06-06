# JPKIPassContents.AuthenticationRequest

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

The user authentification request based on the generics type.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
struct AuthenticationRequest<IdentityType> where IdentityType : JPKIPassContents.Identity
```

#### Overview

Use this structure to define valid user authentication request options for `UserIdentity` or `SigningIdentity`.

## Topics

### Creating authentication request options
- [init(type: JPKIPassContents.UserIdentity.AuthenticationType)](jpkipasscontents/authenticationrequest/init(type:)-hz9q.md)
  Initializes the user authentication request options for the user identity type.
- [init(type: JPKIPassContents.SigningIdentity.AuthenticationType)](jpkipasscontents/authenticationrequest/init(type:)-25dbn.md)
  Initializes the user authentication request options for the signing identity type.

## See Also

- [JPKIPassContents.UserIdentity](jpkipasscontents/useridentity-swift.struct.md)
  The functionality for the type of user identification.
- [JPKIPassContents.SigningIdentity](jpkipasscontents/signingidentity-swift.struct.md)
  The authentication for signing user identification.
- [JPKIPassContents.Signature](jpkipasscontents/signature.md)
  The resulting signed data and certificate you use to sign the pass.
- [JPKIPassContents.Certificate](jpkipasscontents/certificate.md)
  The certificate data associated with an identity document.
- [JPKIPassContents.Identity](jpkipasscontents/identity.md)
  Defines the common functionality that JPKI digital identities support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/authenticationrequest)*