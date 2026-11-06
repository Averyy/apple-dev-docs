# OpenID4VPRequest.RequestAuthentication

**Framework**: IdentityDocumentServices  
**Kind**: struct  
**Role**: Structure

A relying party identity that a request signature claims.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
struct RequestAuthentication
```

## Topics

### Initializers
- [init(prefix: OpenID4VPRequest.ClientIdentifierPrefix?, identifier: String, certificateChain: [SecCertificate])](./requestauthentication/init%28prefix,identifier,certificatechain%29.md)
  Initializes a request authentication.
### Instance Properties
- [var certificateChain: [SecCertificate]](./requestauthentication/certificatechain.md)
  The certificate chain that the request presents for an identifier.
- [var clientIdentifier: String](./requestauthentication/clientidentifier.md)
  The `client_id` value as it appears in the request.
- [var identifier: String](./requestauthentication/identifier.md)
  The identifier for the relying party.
- [var prefix: OpenID4VPRequest.ClientIdentifierPrefix?](./requestauthentication/prefix.md)
  The prefix that determines the method for establishing the relying party’s identity.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Authenticating the relying party
- [var requestAuthentications: [OpenID4VPRequest.RequestAuthentication]](./requestauthentications.md)
  An array that contains information about the authentication of the OpenID4VP request.
- [OpenID4VPRequest.ClientIdentifierPrefix](./clientidentifierprefix.md)
  A client identifier prefix that determines the method for establishing a relying party’s identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/openid4vprequest/requestauthentication)*