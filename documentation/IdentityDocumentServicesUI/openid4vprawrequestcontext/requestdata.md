# requestData

**Framework**: IdentityDocumentServicesUI  
**Kind**: property  
**Role**: Instance Property

Incoming request data that uses encoding the exchange protocol defines.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst

## Declaration

```swift
let requestData: Data
```

## Discussion

Use [`exchangeProtocol`](./exchangeprotocol.md) to determine how to decode this data.

## See Also

### Reading the request
- [let exchangeProtocol: OpenID4VPExchangeProtocolIdentifier](./exchangeprotocol.md)
  The protocol identifier that determines the format of the request and response data.
- [let requestingWebsiteOrigin: URL?](./requestingwebsiteorigin.md)
  The origin of the requesting website, if present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/openid4vprawrequestcontext/requestdata)*