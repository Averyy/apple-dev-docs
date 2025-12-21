# ISO18013MobileDocumentRequestScene

**Framework**: IdentityDocumentServicesUI  
**Kind**: struct

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
@MainActor
@preconcurrency struct ISO18013MobileDocumentRequestScene<Content> where Content : Sendable, Content : View
```

## Topics

### Initializers
- [init(content: (ISO18013MobileDocumentRequestContext) -> Content)](iso18013mobiledocumentrequestscene/init(content:).md)
  Initialize an ISO 18013 mobile document raw request scene.

## Relationships

### Conforms To
- [AppExtensionScene](../ExtensionKit/AppExtensionScene.md)
- [IdentityDocumentRequestScene](identitydocumentrequestscene.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol IdentityDocumentProvider](identitydocumentprovider.md)
  An app extension that provides an identity document.
- [protocol IdentityDocumentRequestScene](identitydocumentrequestscene.md)
  A scene that indicates support for a specific document request type.
- [struct ISO18013MobileDocumentRequestContext](iso18013mobiledocumentrequestcontext.md)
  An object that contains details about the ISO 18013 mobile document request.
- [struct IdentityDocumentRequestSceneBuilder](identitydocumentrequestscenebuilder.md)
  A result builder that combines one or more `IdentityDocumentRequestScene`s into a single scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/iso18013mobiledocumentrequestscene)*