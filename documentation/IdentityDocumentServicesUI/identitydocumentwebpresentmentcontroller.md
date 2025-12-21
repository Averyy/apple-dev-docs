# IdentityDocumentWebPresentmentController

**Framework**: IdentityDocumentServicesUI  
**Kind**: class

A controller that performs identity document requests originating from the web.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
@MainActor
final class IdentityDocumentWebPresentmentController
```

## Topics

### Initializers
- [init()](identitydocumentwebpresentmentcontroller/init.md)
  Initialize a web presentment controller.
### Instance Properties
- [var delegate: (any IdentityDocumentWebPresentmentControllerDelegate)?](identitydocumentwebpresentmentcontroller/delegate.md)
  A delegate that provides information for the controller to perform a web presentment.
- [var presentationContextProvider: (any IdentityDocumentPresentmentControllerPresentationContextProviding)?](identitydocumentwebpresentmentcontroller/presentationcontextprovider.md)
  A delegate that provides a display context in which the system can present an authorization interface to the user.
### Instance Methods
- [func performRequests([any IdentityDocumentWebPresentmentRequest], origin: URL) async throws -> any IdentityDocumentWebPresentmentResponse](identitydocumentwebpresentmentcontroller/performrequests(_:origin:).md)
  Performs an identity document request.

## Relationships

### Conforms To
- [IdentityDocumentPresentmentControlling](identitydocumentpresentmentcontrolling.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Implementing as an identity document provider](../IdentityDocumentServices/Implenting-as-an-identity-document-provider.md)
  Add your app as an option for mobile document web presentment.
- [protocol IdentityDocumentWebPresentmentControllerDelegate](identitydocumentwebpresentmentcontrollerdelegate.md)
  Defines a delegate that the system uses in conjunction with a web presentment controller.
- [protocol IdentityDocumentPresentmentControllerPresentationContextProviding](identitydocumentpresentmentcontrollerpresentationcontextproviding.md)
  An interface the controller uses to receive a presentation context.
- [typealias IdentityDocumentPresentationAnchor](identitydocumentpresentationanchor.md)
  The presentation anchor the system uses to present your app UI.
- [protocol IdentityDocumentPresentmentControlling](identitydocumentpresentmentcontrolling.md)
  A closed protocol that indicates this object is a controller that the system uses for identity document presentment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentwebpresentmentcontroller)*