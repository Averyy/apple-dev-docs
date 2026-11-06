# sendResponse(_:)

**Framework**: IdentityDocumentServicesUI  
**Kind**: method  
**Role**: Instance Method

Sends a document response to the relying party.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst

## Declaration

```swift
func sendResponse(_ response: ISO18013MobileDocumentResponse)
```

## Discussion

Call this method after the person using your app authorizes the release of the requested data. To decline the request, call [`cancel()`](./cancel%28%29.md).

## Parameters

- `response`: An [`ISO18013MobileDocumentResponse`](../../IdentityDocumentServices/iso18013mobiledocumentresponse.md) that contains the response data to send to the relying party.

## See Also

### Responding to the request
- [func cancel()](./cancel%28%29.md)
  Cancels the current request from the relying party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/iso18013mobiledocumentrawrequestcontext/sendresponse(_:))*