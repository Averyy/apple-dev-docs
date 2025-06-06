# IdentityType

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: associatedtype  
**Required**: Yes

The type associated with the protocol.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
associatedtype IdentityType : JPKIPassContents.Identity
```

## See Also

- [func certificate(using: JPKIPassContents.AuthenticationRequest<Self.IdentityType>) async throws -> JPKIPassContents.Certificate<Self.IdentityType>](jpkipasscontents/identity/certificate(using:).md)
  The certificate associated with the Identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/identity/identitytype)*