# JPKIPassContents.UserIdentity

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct  
**Role**: Structure

The functionality for the type of user identification.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
struct UserIdentity
```

## Overview

A type of digital identity that the applet can store.

## Topics

### Identifying the pass user
- [let userIdentity: JPKIPassContents.UserIdentity?](./useridentity-swift.property.md)
  Allows for access to the user identity, if present in the JPKI applet.
- [func changePIN(from: String, to: String) async throws](./useridentity-swift.struct/changepin%28from,to%29.md)
  A function that allows for the change of the PIN associated with the user identity.
- [JPKIPassContents.UserIdentity.AuthenticationType](./useridentity-swift.struct/authenticationtype.md)
  Defines valid authentication types associated with the user identity.
### Instance Properties
- [var authenticationTriesRemaining: Int](./useridentity-swift.struct/authenticationtriesremaining.md)
  The tries remaining before the underlying credential locks itself

## Relationships

### Conforms To
- [JPKIPassContents.Identity](./identity.md)

## See Also

### Defining access to the identity passes
- [JPKIPassContents.SigningIdentity](./signingidentity-swift.struct.md)
  The authentication for signing user identification.
- [JPKIPassContents.Signature](./signature.md)
  The resulting signed data and certificate you use to sign the pass.
- [JPKIPassContents.Certificate](./certificate.md)
  The certificate data associated with an identity document.
- [JPKIPassContents.AuthenticationRequest](./authenticationrequest.md)
  The user authentification request based on the generics type.
- [JPKIPassContents.Identity](./identity.md)
  Defines the common functionality that JPKI digital identities support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/useridentity-swift.struct)*