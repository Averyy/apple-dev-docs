# IdentityDocumentServicesUI

**Framework**: IdentityDocumentServicesUI  
**Kind**: module

Provide an interface so people can present mobile documents.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)

#### Overview

The `IdentityDocumentServicesUI` framework contains user-interface objects that support the features in [`IdentityDocumentServices`](https://developer.apple.com/documentation/IdentityDocumentServices). This includes types for implementing authorization UI for an [`IdentityDocumentProvider`](identitydocumentprovider.md) app. It also includes a controller to enable browsers to implement the Digital Credentials API.

## Topics

### Building identity document provider authorization UI
- [protocol IdentityDocumentProvider](identitydocumentprovider.md)
  An app extension that provides an identity document.
- [protocol IdentityDocumentRequestScene](identitydocumentrequestscene.md)
  A scene that indicates support for a specific document request type.
- [struct ISO18013MobileDocumentRequestScene](iso18013mobiledocumentrequestscene.md)
- [struct ISO18013MobileDocumentRequestContext](iso18013mobiledocumentrequestcontext.md)
  An object that contains details about the ISO 18013 mobile document request.
- [struct IdentityDocumentRequestSceneBuilder](identitydocumentrequestscenebuilder.md)
  A result builder that combines one or more `IdentityDocumentRequestScene`s into a single scene.
### Implementing the web presentment flow into your browser
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
- [protocol IdentityDocumentPresentmentControlling](identitydocumentpresentmentcontrolling.md)
  A closed protocol that indicates this object is a controller that the system uses for identity document presentment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/IdentityDocumentServicesUI)*