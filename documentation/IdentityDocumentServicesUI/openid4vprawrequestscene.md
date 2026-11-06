# OpenID4VPRawRequestScene

**Framework**: IdentityDocumentServicesUI  
**Kind**: struct  
**Role**: Structure

A scene that indicates support for the request format defined in OpenID for Verifiable Presentations.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst

## Declaration

```swift
@MainActor
@preconcurrency struct OpenID4VPRawRequestScene<Content> where Content : View
```

## Overview

The system displays the UI content in this scene when a person using your app selects it. Include information about the requested credentials and the relying party requesting the data, if possible. The content also gives the person the option to authorize the release of the credentials to the relying party, or to cancel the current request and not release any data.

The scene provides the request through an [`OpenID4VPRawRequestContext`](./openid4vprawrequestcontext.md).

## Topics

### Creating a scene
- [init(content: (OpenID4VPRawRequestContext) -> Content)](./openid4vprawrequestscene/init%28content%29.md)
  Creates a request scene for handling a full OpenID4VP mobile document raw request.

## Relationships

### Conforms To
- [AppExtensionScene](../ExtensionKit/appextensionscene.md)
- [IdentityDocumentRequestScene](./identitydocumentrequestscene.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Handling raw requests
- [struct ISO18013MobileDocumentRawRequestScene](./iso18013mobiledocumentrawrequestscene.md)
  A scene that indicates support for the request type defined in ISO 18013.
- [struct ISO18013MobileDocumentRawRequestContext](./iso18013mobiledocumentrawrequestcontext.md)
  A context that contains an incoming ISO 18013 mobile document request.
- [struct OpenID4VPRawRequestContext](./openid4vprawrequestcontext.md)
  A context that contains an incoming OpenID4VP request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/openid4vprawrequestscene)*