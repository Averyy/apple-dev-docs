# ISO18013MobileDocumentRequest

**Framework**: IdentityDocumentServices  
**Kind**: struct

A type that represents an incoming ISO 18013-5 mobile document request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
struct ISO18013MobileDocumentRequest
```

## Topics

### Structures
- [ISO18013MobileDocumentRequest.DocumentRequest](iso18013mobiledocumentrequest/documentrequest.md)
  A request that contains information for requesting a mobile document.
- [ISO18013MobileDocumentRequest.DocumentRequestSet](iso18013mobiledocumentrequest/documentrequestset.md)
  A set of document requests defined in a `PresentmentRequest`.
- [ISO18013MobileDocumentRequest.ElementInfo](iso18013mobiledocumentrequest/elementinfo.md)
  A type that contains request information about an element.
- [ISO18013MobileDocumentRequest.PresentmentRequest](iso18013mobiledocumentrequest/presentmentrequest.md)
  A type that represents an individual presentment request.
- [ISO18013MobileDocumentRequest.RequestAuthentication](iso18013mobiledocumentrequest/requestauthentication.md)
  A type that contains information for authenticating the incoming request.
### Initializers
- [init(presentmentRequests: [ISO18013MobileDocumentRequest.PresentmentRequest], requestAuthentications: [ISO18013MobileDocumentRequest.RequestAuthentication])](iso18013mobiledocumentrequest/init(presentmentrequests:requestauthentications:).md)
  Initializes an ISO 18013-5 mobile document request.
### Instance Properties
- [var presentmentRequests: [ISO18013MobileDocumentRequest.PresentmentRequest]](iso18013mobiledocumentrequest/presentmentrequests.md)
  An array of the presentment requests that exist in the incoming mobile document request.
- [var requestAuthentications: [ISO18013MobileDocumentRequest.RequestAuthentication]](iso18013mobiledocumentrequest/requestauthentications.md)
  An array that contains information about the authentication of the mobile document request.

## Relationships

### Conforms To
- [IdentityDocumentWebPresentmentRequest](identitydocumentwebpresentmentrequest.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct IdentityDocumentWebPresentmentRawRequestValidator](identitydocumentwebpresentmentrawrequestvalidator.md)
  A type that contains functions for validating the incoming web presentment raw request.
- [protocol IdentityDocumentWebPresentmentRequest](identitydocumentwebpresentmentrequest.md)
  A closed protocol that indicates that the system uses this object to perform an identity document web presentment
- [protocol IdentityDocumentWebPresentmentResponse](identitydocumentwebpresentmentresponse.md)
  A closed protocol that indicates that the system uses this object to represent a web presentment response.
- [struct ISO18013MobileDocumentResponse](iso18013mobiledocumentresponse.md)
  A type representing the document response from a web presentment request.
- [struct IdentityDocumentWebPresentmentRawRequest](identitydocumentwebpresentmentrawrequest.md)
  A struct that defines the type that represents a raw web presentment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/iso18013mobiledocumentrequest)*