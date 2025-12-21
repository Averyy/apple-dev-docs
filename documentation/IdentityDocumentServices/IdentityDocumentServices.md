# IdentityDocumentServices

**Framework**: IdentityDocumentServices  
**Kind**: module

Share mobile documents using the Digital Credentials API.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+

#### Overview

Identity Document Services enables the presentment of identity documents on device and web browser support for the Digital Credentials API.

![A conceptual image that shows a small identity document and a rectangular web page.](https://docs-assets.developer.apple.com/published/fe83fe395f5f3bb1f92833a0c1798345/identity-document-services-hero~dark%402x.png)

Once authorized, a person can select your app during a identity documents request, where they can authorize the presentment of identification through a UI you create with [`IdentityDocumentServicesUI`](https://developer.apple.com/documentation/IdentityDocumentServicesUI).

This framework also enables web browsers to implement the presentment flow for the Digital Credentials API. With web browser support, a person can present identity documents locally on their device or remotely on another device using the same iCloud account. Identity documents can include documents such as a driver’s license or identity card.

## Topics

### Essentials
- [Requesting a mobile document on the web](requesting-a-mobile-document-on-the-web.md)
  Send a request for mobile document information for apps installed on a device.
- [Implementing as an identity document provider](implenting-as-an-identity-document-provider.md)
  Add your app as an option for mobile document web presentment.
### Registering as an identity document provider
- [actor IdentityDocumentProviderRegistrationStore](identitydocumentproviderregistrationstore.md)
  A store that notifies the system which documents an app has available for presentment.
- [protocol IdentityDocumentRegistration](identitydocumentregistration.md)
  A protocol that defines an identity document registration.
- [struct MobileDocumentRegistration](mobiledocumentregistration.md)
  A type you use to register mobile documents.
### Implementing the web presentment flow into your browser
- [struct IdentityDocumentWebPresentmentRawRequestValidator](identitydocumentwebpresentmentrawrequestvalidator.md)
  A type that contains functions for validating the incoming web presentment raw request.
- [protocol IdentityDocumentWebPresentmentRequest](identitydocumentwebpresentmentrequest.md)
  A closed protocol that indicates that the system uses this object to perform an identity document web presentment
- [struct ISO18013MobileDocumentRequest](iso18013mobiledocumentrequest.md)
  A type that represents an incoming ISO 18013-5 mobile document request.
- [protocol IdentityDocumentWebPresentmentResponse](identitydocumentwebpresentmentresponse.md)
  A closed protocol that indicates that the system uses this object to represent a web presentment response.
- [struct ISO18013MobileDocumentResponse](iso18013mobiledocumentresponse.md)
  A type representing the document response from a web presentment request.
- [struct IdentityDocumentWebPresentmentRawRequest](identitydocumentwebpresentmentrawrequest.md)
  A struct that defines the type that represents a raw web presentment request.
### Structures
- [struct IdentityDocumentPresentmentError](identitydocumentpresentmenterror.md)
  An error type that is thrown from the identity document web presentment controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/IdentityDocumentServices)*