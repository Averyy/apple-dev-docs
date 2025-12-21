# presentationAnchorForPresentmentController(_:)

**Framework**: IdentityDocumentServicesUI  
**Kind**: method  
**Required**: Yes

Indicates the presentation anchor within which the system presents the controller’s UI to the presentment controller.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
@MainActor
func presentationAnchorForPresentmentController(_ presentmentController: any IdentityDocumentPresentmentControlling) -> IdentityDocumentPresentationAnchor?
```

#### Return Value

The presentation anchor the system uses to present UI.

#### Discussion

Returning `nil` from this method results in an `IdentityDocumentWebPresentmentError/invalidRequest` error when performing an authorization request.

## Parameters

- `presentmentController`: The active presentment controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentpresentmentcontrollerpresentationcontextproviding/presentationanchorforpresentmentcontroller(_:)-26ohw)*