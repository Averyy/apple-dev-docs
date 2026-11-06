# x509Hash

**Framework**: IdentityDocumentServices  
**Kind**: property  
**Role**: Type Property

A prefix for the relying party that identify themselves with the hash of an X.509 certificate.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
static let x509Hash: OpenID4VPRequest.ClientIdentifierPrefix
```

## See Also

### Getting standard prefixes
- [static let decentralizedIdentifier: OpenID4VPRequest.ClientIdentifierPrefix](./decentralizedidentifier.md)
  A prefix for requesters that identify themselves with a decentralized identifier (DID).
- [static let openIDFederation: OpenID4VPRequest.ClientIdentifierPrefix](./openidfederation.md)
  A prefix for requesters that identify themselves through an OpenID Federation.
- [static let verifierAttestation: OpenID4VPRequest.ClientIdentifierPrefix](./verifierattestation.md)
  A prefix for a relying party that receives a request and identifies themselves with authentication from a trusted party.
- [static let x509_SAN_DNS: OpenID4VPRequest.ClientIdentifierPrefix](./x509_san_dns.md)
  A prefix for the relying party that identify themselves with a DNS name in an X.509 certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/openid4vprequest/clientidentifierprefix/x509hash)*