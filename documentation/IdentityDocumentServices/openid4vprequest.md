# OpenID4VPRequest

**Framework**: IdentityDocumentServices  
**Kind**: struct  
**Role**: Structure

A type that represents an incoming OpenID for Verifiable Presentations request.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
struct OpenID4VPRequest
```

## Topics

### Creating a request
- [init(exchangeProtocol: OpenID4VPExchangeProtocolIdentifier, query: DigitalCredentialsQuery, requestAuthentications: [OpenID4VPRequest.RequestAuthentication])](./openid4vprequest/init%28exchangeprotocol,query,requestauthentications%29.md)
  Initializes an OpenID4VP request.
### Inspecting a request
- [var exchangeProtocol: OpenID4VPExchangeProtocolIdentifier](./openid4vprequest/exchangeprotocol.md)
  The exchange protocol used for the request.
- [var query: DigitalCredentialsQuery](./openid4vprequest/query.md)
  The credentials and claims the relying party requests.
### Authenticating the relying party
- [var requestAuthentications: [OpenID4VPRequest.RequestAuthentication]](./openid4vprequest/requestauthentications.md)
  An array that contains information about the authentication of the OpenID4VP request.
- [OpenID4VPRequest.RequestAuthentication](./openid4vprequest/requestauthentication.md)
  A relying party identity that a request signature claims.
- [OpenID4VPRequest.ClientIdentifierPrefix](./openid4vprequest/clientidentifierprefix.md)
  A client identifier prefix that determines the method for establishing a relying party’s identity.

## Relationships

### Conforms To
- [IdentityDocumentWebPresentmentRequest](./identitydocumentwebpresentmentrequest.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Requesting credentials with OpenID4VP
- [struct OpenID4VPResponse](./openid4vpresponse.md)
  A response to an OpenID4VP request.
- [enum OpenID4VPExchangeProtocolIdentifier](./openid4vpexchangeprotocolidentifier.md)
  A value that identifies which OpenID4VP exchange protocol a request or response uses.
- [struct DigitalCredentialsQuery](./digitalcredentialsquery.md)
  A request that describes the credentials and claims a relying party wants from a person’s digital ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/openid4vprequest)*