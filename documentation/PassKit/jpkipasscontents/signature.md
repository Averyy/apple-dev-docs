# JPKIPassContents.Signature

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct  
**Role**: Structure

The resulting signed data and certificate you use to sign the pass.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
struct Signature<IdentityType> where IdentityType : JPKIPassContents.Identity
```

#### Overview

Use this structure to access the signature associated with digital identities.

## Topics

### Defining the certificate and signed data
- [let certificate: JPKIPassContents.Certificate<IdentityType>](./signature/certificate.md)
  The certificate associated with an identity document.
- [let signatureData: Data](./signature/signaturedata.md)
  The result of signing the data provided by the caller using the requested digital identity.

## See Also

### Defining access to the identity passes
- [JPKIPassContents.UserIdentity](./useridentity-swift.struct.md)
  The functionality for the type of user identification.
- [JPKIPassContents.SigningIdentity](./signingidentity-swift.struct.md)
  The authentication for signing user identification.
- [JPKIPassContents.Certificate](./certificate.md)
  The certificate data associated with an identity document.
- [JPKIPassContents.AuthenticationRequest](./authenticationrequest.md)
  The user authentification request based on the generics type.
- [JPKIPassContents.Identity](./identity.md)
  Defines the common functionality that JPKI digital identities support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/signature)*