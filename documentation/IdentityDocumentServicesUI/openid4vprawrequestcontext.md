# OpenID4VPRawRequestContext

**Framework**: IdentityDocumentServicesUI  
**Kind**: struct  
**Role**: Structure

A context that contains an incoming OpenID4VP request.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst

## Declaration

```swift
struct OpenID4VPRawRequestContext
```

## Overview

OpenID for Verifiable Presentations (OpenID4VP) is a protocol that relying parties use to request credentials. The system provides this context to the closure you pass to [`init(content:)`](./openid4vprawrequestscene/init%28content%29.md). A *relying party* is the website, app, or service that asks to see that information and then relies on it to make a decision, such as confirming a person’s age or identity. Read the request from [`requestData`](./openid4vprawrequestcontext/requestdata.md), using [`exchangeProtocol`](./openid4vprawrequestcontext/exchangeprotocol.md) to determine how to decode the data, and present the request to the person using your app. To release credentials, call [`sendResponse(_:)`](./openid4vprawrequestcontext/sendresponse%28_%29.md) with an [`OpenID4VPRawRequestContext.Response`](./openid4vprawrequestcontext/response.md). To decline, call [`cancel()`](./openid4vprawrequestcontext/cancel%28%29.md).

## Topics

### Reading the request
- [let requestData: Data](./openid4vprawrequestcontext/requestdata.md)
  Incoming request data that uses encoding the exchange protocol defines.
- [let exchangeProtocol: OpenID4VPExchangeProtocolIdentifier](./openid4vprawrequestcontext/exchangeprotocol.md)
  The protocol identifier that determines the format of the request and response data.
- [let requestingWebsiteOrigin: URL?](./openid4vprawrequestcontext/requestingwebsiteorigin.md)
  The origin of the requesting website, if present.
### Responding to the request
- [func sendResponse(OpenID4VPRawRequestContext.Response)](./openid4vprawrequestcontext/sendresponse%28_%29.md)
  Sends an OpenID4VP response to the relying party.
- [OpenID4VPRawRequestContext.Response](./openid4vprawrequestcontext/response.md)
  An OpenID4VP response to send to the relying party.
- [func cancel()](./openid4vprawrequestcontext/cancel%28%29.md)
  Cancels the current request from the relying party.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Handling raw requests
- [struct ISO18013MobileDocumentRawRequestScene](./iso18013mobiledocumentrawrequestscene.md)
  A scene that indicates support for the request type defined in ISO 18013.
- [struct ISO18013MobileDocumentRawRequestContext](./iso18013mobiledocumentrawrequestcontext.md)
  A context that contains an incoming ISO 18013 mobile document request.
- [struct OpenID4VPRawRequestScene](./openid4vprawrequestscene.md)
  A scene that indicates support for the request format defined in OpenID for Verifiable Presentations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/openid4vprawrequestcontext)*