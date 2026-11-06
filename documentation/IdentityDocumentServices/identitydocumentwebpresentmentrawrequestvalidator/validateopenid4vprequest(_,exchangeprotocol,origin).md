# validateOpenID4VPRequest(_:exchangeProtocol:origin:)

**Framework**: IdentityDocumentServices  
**Kind**: method  
**Role**: Instance Method

Validates an incoming raw OpenID4VP request.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst
- macOS 27.3+ (Beta)

## Declaration

```swift
func validateOpenID4VPRequest(_ requestData: Data, exchangeProtocol: OpenID4VPExchangeProtocolIdentifier, origin: URL) throws -> OpenID4VPRequest
```

## Return Value

The validated OpenID4VP request.

## Parameters

- `requestData`: The request data from the caller.
- `exchangeProtocol`: The exchange protocol that the request uses.
- `origin`: The origin of the requesting website.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentwebpresentmentrawrequestvalidator/validateopenid4vprequest(_:exchangeprotocol:origin:))*