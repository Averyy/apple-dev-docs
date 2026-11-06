# OpenID4VPExchangeProtocolIdentifier

**Framework**: IdentityDocumentServices  
**Kind**: enum  
**Role**: Enumeration

A value that identifies which OpenID4VP exchange protocol a request or response uses.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
enum OpenID4VPExchangeProtocolIdentifier
```

## Topics

### Enumeration Cases
- [OpenID4VPExchangeProtocolIdentifier.multisignedV1](./openid4vpexchangeprotocolidentifier/multisignedv1.md)
  A value that corresponds to an OpenID4VP multisigned exchange protocol.
- [OpenID4VPExchangeProtocolIdentifier.signedV1](./openid4vpexchangeprotocolidentifier/signedv1.md)
  A value that corresponds to an OpenID4VP signed exchange protocol.
- [OpenID4VPExchangeProtocolIdentifier.unsignedV1](./openid4vpexchangeprotocolidentifier/unsignedv1.md)
  A value that corresponds to an OpenID4VP unsigned exchange protocol.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Requesting credentials with OpenID4VP
- [struct OpenID4VPRequest](./openid4vprequest.md)
  A type that represents an incoming OpenID for Verifiable Presentations request.
- [struct OpenID4VPResponse](./openid4vpresponse.md)
  A response to an OpenID4VP request.
- [struct DigitalCredentialsQuery](./digitalcredentialsquery.md)
  A request that describes the credentials and claims a relying party wants from a person’s digital ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/openid4vpexchangeprotocolidentifier)*