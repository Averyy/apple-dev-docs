# IdentityDocumentRequestSceneBuilder

**Framework**: IdentityDocumentServicesUI  
**Kind**: struct

A result builder that combines one or more `IdentityDocumentRequestScene`s into a single scene.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
@MainActor
@resultBuilder struct IdentityDocumentRequestSceneBuilder
```

## Topics

### Type Methods
- [static func buildBlock(some IdentityDocumentRequestScene) -> some IdentityDocumentRequestScene](identitydocumentrequestscenebuilder/buildblock(_:).md)
  A result builder that combines one or more identity document request scene`s into a single scene.
- [static func buildBlock(some IdentityDocumentRequestScene, some IdentityDocumentRequestScene) -> some IdentityDocumentRequestScene](identitydocumentrequestscenebuilder/buildblock(_:_:).md)
  A result builder that combines one or more identity document request scene`s into a single scene.
- [static func buildLimitedAvailability(some IdentityDocumentRequestScene) -> some IdentityDocumentRequestScene](identitydocumentrequestscenebuilder/buildlimitedavailability(_:).md)
- [static func buildOptional((some IdentityDocumentRequestScene)?) -> some IdentityDocumentRequestScene](identitydocumentrequestscenebuilder/buildoptional(_:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol IdentityDocumentProvider](identitydocumentprovider.md)
  An app extension that provides an identity document.
- [protocol IdentityDocumentRequestScene](identitydocumentrequestscene.md)
  A scene that indicates support for a specific document request type.
- [struct ISO18013MobileDocumentRequestScene](iso18013mobiledocumentrequestscene.md)
- [struct ISO18013MobileDocumentRequestContext](iso18013mobiledocumentrequestcontext.md)
  An object that contains details about the ISO 18013 mobile document request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentrequestscenebuilder)*