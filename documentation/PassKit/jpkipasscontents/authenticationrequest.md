# JPKIPassContents.AuthenticationRequest

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct  
**Role**: Structure

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
- [init(type: JPKIPassContents.UserIdentity.AuthenticationType)](./authenticationrequest/init%28type%29-hz9q.md)
  Initializes the user authentication request options for the user identity type.
- [init(type: JPKIPassContents.SigningIdentity.AuthenticationType)](./authenticationrequest/init%28type%29-25dbn.md)
  Initializes the user authentication request options for the signing identity type.

## See Also

### Defining access to the identity passes
- [JPKIPassContents.UserIdentity](./useridentity-swift.struct.md)
  The functionality for the type of user identification.
- [JPKIPassContents.SigningIdentity](./signingidentity-swift.struct.md)
  The authentication for signing user identification.
- [JPKIPassContents.Signature](./signature.md)
  The resulting signed data and certificate you use to sign the pass.
- [JPKIPassContents.Certificate](./certificate.md)
  The certificate data associated with an identity document.
- [JPKIPassContents.Identity](./identity.md)
  Defines the common functionality that JPKI digital identities support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/authenticationrequest)*