# sendResponse(_:)

**Framework**: IdentityDocumentServicesUI  
**Kind**: method  
**Role**: Instance Method

Sends an OpenID4VP response to the relying party.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst

## Declaration

```swift
func sendResponse(_ response: OpenID4VPRawRequestContext.Response)
```

## Discussion

Call this method after the person using your app authorizes the release of the requested credentials. To decline the request, call [`cancel()`](./cancel%28%29.md).

## Parameters

- `response`: An [`OpenID4VPRawRequestContext.Response`](./response.md) that contains the OpenID4VP authorization response to send to the relying party.

## See Also

### Responding to the request
- [OpenID4VPRawRequestContext.Response](./response.md)
  An OpenID4VP response to send to the relying party.
- [func cancel()](./cancel%28%29.md)
  Cancels the current request from the relying party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/openid4vprawrequestcontext/sendresponse(_:))*