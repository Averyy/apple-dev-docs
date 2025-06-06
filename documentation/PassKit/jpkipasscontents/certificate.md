# JPKIPassContents.Certificate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

The certificate data associated with an identity document.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
struct Certificate<IdentityType> where IdentityType : JPKIPassContents.Identity
```

#### Overview

Use this structure to access the underlying certificate data you use to sign the pass.

## Topics

### Defining data
- [let data: Data](jpkipasscontents/certificate/data.md)
  The result of the signed data from the requested digital identity in X.509 DER format.

## See Also

- [JPKIPassContents.UserIdentity](jpkipasscontents/useridentity-swift.struct.md)
  The functionality for the type of user identification.
- [JPKIPassContents.SigningIdentity](jpkipasscontents/signingidentity-swift.struct.md)
  The authentication for signing user identification.
- [JPKIPassContents.Signature](jpkipasscontents/signature.md)
  The resulting signed data and certificate you use to sign the pass.
- [JPKIPassContents.AuthenticationRequest](jpkipasscontents/authenticationrequest.md)
  The user authentification request based on the generics type.
- [JPKIPassContents.Identity](jpkipasscontents/identity.md)
  Defines the common functionality that JPKI digital identities support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/certificate)*