# JPKIPassContents.Identity

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: protocol

Defines the common functionality that JPKI digital identities support.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
protocol Identity
```

## Topics

### Data associated with the identity
- [associatedtype IdentityType : JPKIPassContents.Identity](jpkipasscontents/identity/identitytype.md)
  The type associated with the protocol.
- [func certificate(using: JPKIPassContents.AuthenticationRequest<Self.IdentityType>) async throws -> JPKIPassContents.Certificate<Self.IdentityType>](jpkipasscontents/identity/certificate(using:).md)
  The certificate associated with the Identity.
### Instance Properties
- [var authenticationTriesRemaining: Int](jpkipasscontents/identity/authenticationtriesremaining.md)
  The tries remaining before the underlying credential locks itself
### Instance Methods
- [func signature(for: [Data], using: JPKIPassContents.AuthenticationRequest<Self.IdentityType>) async throws -> [JPKIPassContents.Signature<Self.IdentityType>]](jpkipasscontents/identity/signature(for:using:)-35arv.md)
  Signs the supplied array of data with the identity’s private key
- [func signature(for: Data, using: JPKIPassContents.AuthenticationRequest<Self.IdentityType>) async throws -> JPKIPassContents.Signature<Self.IdentityType>](jpkipasscontents/identity/signature(for:using:)-4l8jw.md)
  Signs the supplied data with the identity’s private key

## Relationships

### Conforming Types
- [JPKIPassContents.SigningIdentity](jpkipasscontents/signingidentity-swift.struct.md)
- [JPKIPassContents.UserIdentity](jpkipasscontents/useridentity-swift.struct.md)

## See Also

- [JPKIPassContents.UserIdentity](jpkipasscontents/useridentity-swift.struct.md)
  The functionality for the type of user identification.
- [JPKIPassContents.SigningIdentity](jpkipasscontents/signingidentity-swift.struct.md)
  The authentication for signing user identification.
- [JPKIPassContents.Signature](jpkipasscontents/signature.md)
  The resulting signed data and certificate you use to sign the pass.
- [JPKIPassContents.Certificate](jpkipasscontents/certificate.md)
  The certificate data associated with an identity document.
- [JPKIPassContents.AuthenticationRequest](jpkipasscontents/authenticationrequest.md)
  The user authentification request based on the generics type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/identity)*