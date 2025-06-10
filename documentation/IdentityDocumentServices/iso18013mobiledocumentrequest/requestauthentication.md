# ISO18013MobileDocumentRequest.RequestAuthentication

**Framework**: IdentityDocumentServices  
**Kind**: struct

A type that contains information for authenticating the incoming request.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
struct RequestAuthentication
```

## Topics

### Initializers
- [init(authenticationCertificateChain: [SecCertificate])](iso18013mobiledocumentrequest/requestauthentication/init(authenticationcertificatechain:).md)
  Initializes a request authentication.
### Instance Properties
- [var authenticationCertificateChain: [SecCertificate]](iso18013mobiledocumentrequest/requestauthentication/authenticationcertificatechain.md)
  A certificate chain that you use to authenticate the relying party.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/iso18013mobiledocumentrequest/requestauthentication)*