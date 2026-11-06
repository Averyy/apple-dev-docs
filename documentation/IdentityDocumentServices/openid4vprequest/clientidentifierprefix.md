# OpenID4VPRequest.ClientIdentifierPrefix

**Framework**: IdentityDocumentServices  
**Kind**: struct  
**Role**: Structure

A client identifier prefix that determines the method for establishing a relying party’s identity.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
struct ClientIdentifierPrefix
```

## Topics

### Creating a prefix
- [init(rawValue: String)](./clientidentifierprefix/init%28rawvalue%29.md)
  Initializes a client identifier prefix.
- [let rawValue: String](./clientidentifierprefix/rawvalue.md)
  The prefix as it appears in the client identifier.
### Getting standard prefixes
- [static let decentralizedIdentifier: OpenID4VPRequest.ClientIdentifierPrefix](./clientidentifierprefix/decentralizedidentifier.md)
  A prefix for requesters that identify themselves with a decentralized identifier (DID).
- [static let openIDFederation: OpenID4VPRequest.ClientIdentifierPrefix](./clientidentifierprefix/openidfederation.md)
  A prefix for requesters that identify themselves through an OpenID Federation.
- [static let verifierAttestation: OpenID4VPRequest.ClientIdentifierPrefix](./clientidentifierprefix/verifierattestation.md)
  A prefix for a relying party that receives a request and identifies themselves with authentication from a trusted party.
- [static let x509Hash: OpenID4VPRequest.ClientIdentifierPrefix](./clientidentifierprefix/x509hash.md)
  A prefix for the relying party that identify themselves with the hash of an X.509 certificate.
- [static let x509_SAN_DNS: OpenID4VPRequest.ClientIdentifierPrefix](./clientidentifierprefix/x509_san_dns.md)
  A prefix for the relying party that identify themselves with a DNS name in an X.509 certificate.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Authenticating the relying party
- [var requestAuthentications: [OpenID4VPRequest.RequestAuthentication]](./requestauthentications.md)
  An array that contains information about the authentication of the OpenID4VP request.
- [OpenID4VPRequest.RequestAuthentication](./requestauthentication.md)
  A relying party identity that a request signature claims.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/openid4vprequest/clientidentifierprefix)*