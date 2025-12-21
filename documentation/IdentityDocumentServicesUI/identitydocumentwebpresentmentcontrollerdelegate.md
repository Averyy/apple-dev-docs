# IdentityDocumentWebPresentmentControllerDelegate

**Framework**: IdentityDocumentServicesUI  
**Kind**: protocol

Defines a delegate that the system uses in conjunction with a web presentment controller.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
@MainActor
protocol IdentityDocumentWebPresentmentControllerDelegate : AnyObject
```

## Topics

### Instance Methods
- [func rawRequestsForWebPresentmentController(IdentityDocumentWebPresentmentController) async -> [IdentityDocumentWebPresentmentRawRequest]](identitydocumentwebpresentmentcontrollerdelegate/rawrequestsforwebpresentmentcontroller(_:).md)
  A method that allows the calling app to provide the incoming raw web presentment requests to the web presentment controller.

## See Also

- [Implementing as an identity document provider](../IdentityDocumentServices/Implenting-as-an-identity-document-provider.md)
  Add your app as an option for mobile document web presentment.
- [class IdentityDocumentWebPresentmentController](identitydocumentwebpresentmentcontroller.md)
  A controller that performs identity document requests originating from the web.
- [protocol IdentityDocumentPresentmentControllerPresentationContextProviding](identitydocumentpresentmentcontrollerpresentationcontextproviding.md)
  An interface the controller uses to receive a presentation context.
- [typealias IdentityDocumentPresentationAnchor](identitydocumentpresentationanchor.md)
  The presentation anchor the system uses to present your app UI.
- [protocol IdentityDocumentPresentmentControlling](identitydocumentpresentmentcontrolling.md)
  A closed protocol that indicates this object is a controller that the system uses for identity document presentment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentwebpresentmentcontrollerdelegate)*