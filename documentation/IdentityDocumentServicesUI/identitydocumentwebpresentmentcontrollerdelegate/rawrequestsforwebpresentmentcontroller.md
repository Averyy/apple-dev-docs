# rawRequestsForWebPresentmentController(_:)

**Framework**: IdentityDocumentServicesUI  
**Kind**: method  
**Required**: Yes

A method that allows the calling app to provide the incoming raw web presentment requests to the web presentment controller.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
@MainActor
func rawRequestsForWebPresentmentController(_ webPresentmentController: IdentityDocumentWebPresentmentController) async -> [IdentityDocumentWebPresentmentRawRequest]
```

#### Return Value

A list of raw web presentment requests.

#### Discussion

If this method is unimplemented, then an `IdentityDocumentWebPresentmentError/invalidRequest` is thrown from the web presentment controller.

## Parameters

- `webPresentmentController`: The active presentment controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentwebpresentmentcontrollerdelegate/rawrequestsforwebpresentmentcontroller(_:))*