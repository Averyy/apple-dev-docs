# ISO18013MobileDocumentRawRequestScene

**Framework**: IdentityDocumentServicesUI  
**Kind**: struct  
**Role**: Structure

A scene that indicates support for the request type defined in ISO 18013.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst

## Declaration

```swift
@MainActor
@preconcurrency struct ISO18013MobileDocumentRawRequestScene<Content> where Content : View
```

## Overview

The system displays the UI content in this scene when the person selects your app when presenting their mobile documents on the web. The content includes information about the requested document and the relying party requesting the data, if possible. Give the person the option to authorize the release of the document to the relying party, or to cancel the current request and not release any data.

Unlike [`ISO18013MobileDocumentRequestScene`](./iso18013mobiledocumentrequestscene.md), this scene provides the unparsed request through an [`ISO18013MobileDocumentRawRequestContext`](./iso18013mobiledocumentrawrequestcontext.md), so you can interpret the request data yourself.

## Topics

### Creating a scene
- [init(content: (ISO18013MobileDocumentRawRequestContext) -> Content)](./iso18013mobiledocumentrawrequestscene/init%28content%29.md)
  Creates a request scene for handling a full ISO 18013 mobile document raw request.

## Relationships

### Conforms To
- [AppExtensionScene](../ExtensionKit/appextensionscene.md)
- [IdentityDocumentRequestScene](./identitydocumentrequestscene.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Handling raw requests
- [struct ISO18013MobileDocumentRawRequestContext](./iso18013mobiledocumentrawrequestcontext.md)
  A context that contains an incoming ISO 18013 mobile document request.
- [struct OpenID4VPRawRequestScene](./openid4vprawrequestscene.md)
  A scene that indicates support for the request format defined in OpenID for Verifiable Presentations.
- [struct OpenID4VPRawRequestContext](./openid4vprawrequestcontext.md)
  A context that contains an incoming OpenID4VP request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/iso18013mobiledocumentrawrequestscene)*