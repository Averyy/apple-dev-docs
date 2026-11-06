# cancel()

**Framework**: IdentityDocumentServicesUI  
**Kind**: method  
**Role**: Instance Method

Cancels the current request from the relying party.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst

## Declaration

```swift
func cancel()
```

## Discussion

Call this method when the person using your app declines the request. The system doesn’t release any data to the relying party.

## See Also

### Responding to the request
- [func sendResponse(OpenID4VPRawRequestContext.Response)](./sendresponse%28_%29.md)
  Sends an OpenID4VP response to the relying party.
- [OpenID4VPRawRequestContext.Response](./response.md)
  An OpenID4VP response to send to the relying party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/openid4vprawrequestcontext/cancel())*