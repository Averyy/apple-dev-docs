# OpenID4VPResponse

**Framework**: IdentityDocumentServices  
**Kind**: struct  
**Role**: Structure

A response to an OpenID4VP request.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
struct OpenID4VPResponse
```

## Topics

### Creating a response
- [init(exchangeProtocol: OpenID4VPExchangeProtocolIdentifier, responseData: Data)](./openid4vpresponse/init%28exchangeprotocol,responsedata%29.md)
  Initializes an OpenID4VP response.
### Inspecting a response
- [let exchangeProtocol: OpenID4VPExchangeProtocolIdentifier](./openid4vpresponse/exchangeprotocol.md)
  The exchange protocol the response answers.
- [let responseData: Data](./openid4vpresponse/responsedata.md)
  The OpenID4VP authorization response.

## Relationships

### Conforms To
- [IdentityDocumentWebPresentmentResponse](./identitydocumentwebpresentmentresponse.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Requesting credentials with OpenID4VP
- [struct OpenID4VPRequest](./openid4vprequest.md)
  A type that represents an incoming OpenID for Verifiable Presentations request.
- [enum OpenID4VPExchangeProtocolIdentifier](./openid4vpexchangeprotocolidentifier.md)
  A value that identifies which OpenID4VP exchange protocol a request or response uses.
- [struct DigitalCredentialsQuery](./digitalcredentialsquery.md)
  A request that describes the credentials and claims a relying party wants from a person’s digital ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/openid4vpresponse)*