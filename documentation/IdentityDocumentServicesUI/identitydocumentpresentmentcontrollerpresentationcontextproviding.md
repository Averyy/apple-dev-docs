# IdentityDocumentPresentmentControllerPresentationContextProviding

**Framework**: IdentityDocumentServicesUI  
**Kind**: protocol

An interface the controller uses to receive a presentation context.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
protocol IdentityDocumentPresentmentControllerPresentationContextProviding : AnyObject
```

## Topics

### Instance Methods
- [func presentationAnchorForPresentmentController(any IdentityDocumentPresentmentControlling) -> IdentityDocumentPresentationAnchor?](identitydocumentpresentmentcontrollerpresentationcontextproviding/presentationanchorforpresentmentcontroller(_:)-26ohw.md)
  Indicates the presentation anchor within which the system presents the controller’s UI to the presentment controller.
- [func presentationAnchorForPresentmentController(any IdentityDocumentPresentmentControlling) -> IdentityDocumentPresentationAnchor?](identitydocumentpresentmentcontrollerpresentationcontextproviding/presentationanchorforpresentmentcontroller(_:)-58gth.md)
  Indicates the presentation anchor within which the system presents the controller’s UI to the presentment controller.

## See Also

- [Implementing as an identity document provider](../IdentityDocumentServices/Implenting-as-an-identity-document-provider.md)
  Add your app as an option for mobile document web presentment.
- [class IdentityDocumentWebPresentmentController](identitydocumentwebpresentmentcontroller.md)
  A controller that performs identity document requests originating from the web.
- [protocol IdentityDocumentWebPresentmentControllerDelegate](identitydocumentwebpresentmentcontrollerdelegate.md)
  Defines a delegate that the system uses in conjunction with a web presentment controller.
- [typealias IdentityDocumentPresentationAnchor](identitydocumentpresentationanchor.md)
  The presentation anchor the system uses to present your app UI.
- [protocol IdentityDocumentPresentmentControlling](identitydocumentpresentmentcontrolling.md)
  A closed protocol that indicates this object is a controller that the system uses for identity document presentment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentpresentmentcontrollerpresentationcontextproviding)*