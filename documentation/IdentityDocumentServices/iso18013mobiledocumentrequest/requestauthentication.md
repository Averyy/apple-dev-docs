# ISO18013MobileDocumentRequest.RequestAuthentication

**Framework**: IdentityDocumentServices  
**Kind**: struct  
**Role**: Structure

A type that contains information for authenticating the incoming request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst
- macOS 26.0+

## Declaration

```swift
struct RequestAuthentication
```

## Topics

### Initializers
- [init(authenticationCertificateChain: [SecCertificate])](./requestauthentication/init%28authenticationcertificatechain%29.md)
  Initializes a request authentication.
### Instance Properties
- [var authenticationCertificateChain: [SecCertificate]](./requestauthentication/authenticationcertificatechain.md)
  A certificate chain that you use to authenticate the relying party.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/iso18013mobiledocumentrequest/requestauthentication)*