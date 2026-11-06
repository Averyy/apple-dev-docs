# exchangeProtocol

**Framework**: IdentityDocumentServicesUI  
**Kind**: property  
**Role**: Instance Property

The protocol identifier that determines the format of the request and response data.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst

## Declaration

```swift
let exchangeProtocol: OpenID4VPExchangeProtocolIdentifier
```

## Discussion

This value determines how the system encodes [`requestData`](./requestdata.md) and how you format the data in your [`OpenID4VPRawRequestContext.Response`](./response.md).

## See Also

### Reading the request
- [let requestData: Data](./requestdata.md)
  Incoming request data that uses encoding the exchange protocol defines.
- [let requestingWebsiteOrigin: URL?](./requestingwebsiteorigin.md)
  The origin of the requesting website, if present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/openid4vprawrequestcontext/exchangeprotocol)*