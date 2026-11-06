# init(exchangeProtocol:query:requestAuthentications:)

**Framework**: IdentityDocumentServices  
**Kind**: init  
**Role**: Initializer

Initializes an OpenID4VP request.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
init(exchangeProtocol: OpenID4VPExchangeProtocolIdentifier, query: DigitalCredentialsQuery, requestAuthentications: [OpenID4VPRequest.RequestAuthentication])
```

## Parameters

- `exchangeProtocol`: The exchange protocol the request uses.
- `query`: The credentials and claims the relying party requests.
- `requestAuthentications`: An array that contains information about the authentication of the OpenID4VP request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/openid4vprequest/init(exchangeprotocol:query:requestauthentications:))*