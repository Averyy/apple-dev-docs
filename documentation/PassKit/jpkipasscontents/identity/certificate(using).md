# certificate(using:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

The certificate associated with the Identity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func certificate(using request: JPKIPassContents.AuthenticationRequest<Self.IdentityType>) async throws -> JPKIPassContents.Certificate<Self.IdentityType>
```

## Parameters

- `request`: The person’s authentication request used to perform the Identity certificate.

## See Also

### Data associated with the identity
- [associatedtype IdentityType : JPKIPassContents.Identity](./identitytype.md)
  The type associated with the protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/identity/certificate(using:))*