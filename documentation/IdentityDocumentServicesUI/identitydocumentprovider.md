# IdentityDocumentProvider

**Framework**: IdentityDocumentServicesUI  
**Kind**: protocol

An app extension that provides an identity document.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
@MainActor
protocol IdentityDocumentProvider : AppExtension
```

#### Overview

Your extension indicates which request types it supports through the provided `IdentityDocumentRequestScene` concrete types. Based on the request types used by the requesting party, the system presents the UI provided through your app extension to the user when they select your app to respond to a presentment request.

## Topics

### Associated Types
- [associatedtype Body : IdentityDocumentRequestScene](identitydocumentprovider/body-swift.associatedtype.md)
  The type for this provider’s body.
### Instance Properties
- [var body: Self.Body](identitydocumentprovider/body-swift.property.md)
  A body containing an identity document scene for each request type the app supports.
### Instance Methods
- [func performRegistrationUpdates() async](identitydocumentprovider/performregistrationupdates.md)
  A function that allows the current app to perform updates to document registrations to ensure consistency with documents stored in the app.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)

## See Also

- [protocol IdentityDocumentRequestScene](identitydocumentrequestscene.md)
  A scene that indicates support for a specific document request type.
- [struct ISO18013MobileDocumentRequestScene](iso18013mobiledocumentrequestscene.md)
- [struct ISO18013MobileDocumentRequestContext](iso18013mobiledocumentrequestcontext.md)
  An object that contains details about the ISO 18013 mobile document request.
- [struct IdentityDocumentRequestSceneBuilder](identitydocumentrequestscenebuilder.md)
  A result builder that combines one or more `IdentityDocumentRequestScene`s into a single scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentprovider)*