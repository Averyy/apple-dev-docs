# ISO18013MobileDocumentRawRequestContext

**Framework**: IdentityDocumentServicesUI  
**Kind**: struct  
**Role**: Structure

A context that contains an incoming ISO 18013 mobile document request.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst

## Declaration

```swift
struct ISO18013MobileDocumentRawRequestContext
```

## Overview

Use this context when you want to parse a request yourself rather than use the parsed [`request`](./iso18013mobiledocumentrequestcontext/request.md). The system provides the context to the closure you pass to [`init(content:)`](./iso18013mobiledocumentrawrequestscene/init%28content%29.md). Read the JSON-encoded request from [`requestData`](./iso18013mobiledocumentrawrequestcontext/requestdata.md), present it to the person using your app, and call [`sendResponse(_:)`](./iso18013mobiledocumentrawrequestcontext/sendresponse%28_%29.md) with an [`ISO18013MobileDocumentResponse`](../IdentityDocumentServices/iso18013mobiledocumentresponse.md) that contains the document data, or call [`cancel()`](./iso18013mobiledocumentrawrequestcontext/cancel%28%29.md) to decline the request.

## Topics

### Reading the request
- [let requestData: Data](./iso18013mobiledocumentrawrequestcontext/requestdata.md)
  Incoming request data that uses a JSON format the ISO 18013 request profile defines.
- [let requestingWebsiteOrigin: URL?](./iso18013mobiledocumentrawrequestcontext/requestingwebsiteorigin.md)
  The origin of the requesting website, if present.
### Responding to the request
- [func sendResponse(ISO18013MobileDocumentResponse)](./iso18013mobiledocumentrawrequestcontext/sendresponse%28_%29.md)
  Sends a document response to the relying party.
- [func cancel()](./iso18013mobiledocumentrawrequestcontext/cancel%28%29.md)
  Cancels the current request from the relying party.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Handling raw requests
- [struct ISO18013MobileDocumentRawRequestScene](./iso18013mobiledocumentrawrequestscene.md)
  A scene that indicates support for the request type defined in ISO 18013.
- [struct OpenID4VPRawRequestScene](./openid4vprawrequestscene.md)
  A scene that indicates support for the request format defined in OpenID for Verifiable Presentations.
- [struct OpenID4VPRawRequestContext](./openid4vprawrequestcontext.md)
  A context that contains an incoming OpenID4VP request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/iso18013mobiledocumentrawrequestcontext)*