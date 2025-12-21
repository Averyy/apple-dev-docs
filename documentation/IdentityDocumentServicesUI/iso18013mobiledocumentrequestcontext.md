# ISO18013MobileDocumentRequestContext

**Framework**: IdentityDocumentServicesUI  
**Kind**: struct

An object that contains details about the ISO 18013 mobile document request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct ISO18013MobileDocumentRequestContext
```

##### Managing the Context

- [`request`](iso18013mobiledocumentrequestcontext/request.md)
- [`requestingWebsiteOrigin`](iso18013mobiledocumentrequestcontext/requestingwebsiteorigin.md)
- [`sendResponse(_:)`](iso18013mobiledocumentrequestcontext/sendresponse(_:).md)
- [`cancel()`](iso18013mobiledocumentrequestcontext/cancel().md)

## Topics

### Instance Properties
- [let request: ISO18013MobileDocumentRequest](iso18013mobiledocumentrequestcontext/request.md)
  The incoming ISO 18013 mobile document request.
- [let requestingWebsiteOrigin: URL?](iso18013mobiledocumentrequestcontext/requestingwebsiteorigin.md)
  The origin of the requesting website, if present.
### Instance Methods
- [func cancel()](iso18013mobiledocumentrequestcontext/cancel.md)
  Cancels the current request from the relying party.
- [func sendResponse((IdentityDocumentWebPresentmentRawRequest) async throws -> ISO18013MobileDocumentResponse) async throws](iso18013mobiledocumentrequestcontext/sendresponse(_:).md)
  Builds and sends an ISO 18013 mobile document response.

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
- [struct IdentityDocumentRequestSceneBuilder](identitydocumentrequestscenebuilder.md)
  A result builder that combines one or more `IdentityDocumentRequestScene`s into a single scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/iso18013mobiledocumentrequestcontext)*