# IdentityDocumentRequestScene

**Framework**: IdentityDocumentServicesUI  
**Kind**: protocol

A scene that indicates support for a specific document request type.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
@MainActor
@preconcurrency protocol IdentityDocumentRequestScene : AppExtensionScene
```

#### Overview

The framework provides concrete types for this protocol.

## Relationships

### Inherits From
- [AppExtensionScene](../ExtensionKit/AppExtensionScene.md)
### Conforming Types
- [ISO18013MobileDocumentRequestScene](iso18013mobiledocumentrequestscene.md)

## See Also

- [protocol IdentityDocumentProvider](identitydocumentprovider.md)
  An app extension that provides an identity document.
- [struct ISO18013MobileDocumentRequestScene](iso18013mobiledocumentrequestscene.md)
- [struct ISO18013MobileDocumentRequestContext](iso18013mobiledocumentrequestcontext.md)
  An object that contains details about the ISO 18013 mobile document request.
- [struct IdentityDocumentRequestSceneBuilder](identitydocumentrequestscenebuilder.md)
  A result builder that combines one or more `IdentityDocumentRequestScene`s into a single scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentrequestscene)*