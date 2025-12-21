# IdentityDocumentPresentmentControlling

**Framework**: IdentityDocumentServicesUI  
**Kind**: protocol

A closed protocol that indicates this object is a controller that the system uses for identity document presentment.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
@MainActor
protocol IdentityDocumentPresentmentControlling
```

## Relationships

### Conforming Types
- [IdentityDocumentWebPresentmentController](identitydocumentwebpresentmentcontroller.md)

## See Also

- [Implementing as an identity document provider](../IdentityDocumentServices/Implenting-as-an-identity-document-provider.md)
  Add your app as an option for mobile document web presentment.
- [class IdentityDocumentWebPresentmentController](identitydocumentwebpresentmentcontroller.md)
  A controller that performs identity document requests originating from the web.
- [protocol IdentityDocumentWebPresentmentControllerDelegate](identitydocumentwebpresentmentcontrollerdelegate.md)
  Defines a delegate that the system uses in conjunction with a web presentment controller.
- [protocol IdentityDocumentPresentmentControllerPresentationContextProviding](identitydocumentpresentmentcontrollerpresentationcontextproviding.md)
  An interface the controller uses to receive a presentation context.
- [typealias IdentityDocumentPresentationAnchor](identitydocumentpresentationanchor.md)
  The presentation anchor the system uses to present your app UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentpresentmentcontrolling)*