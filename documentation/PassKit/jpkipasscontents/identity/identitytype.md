# IdentityType

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: associatedtype  
**Role**: Associated Type  
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

### Data associated with the identity
- [func certificate(using: JPKIPassContents.AuthenticationRequest<Self.IdentityType>) async throws -> JPKIPassContents.Certificate<Self.IdentityType>](./certificate%28using%29.md)
  The certificate associated with the Identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/identity/identitytype)*