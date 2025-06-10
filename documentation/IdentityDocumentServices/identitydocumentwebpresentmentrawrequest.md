# IdentityDocumentWebPresentmentRawRequest

**Framework**: IdentityDocumentServices  
**Kind**: struct

A struct that defines the type that represents a raw web presentment request.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
struct IdentityDocumentWebPresentmentRawRequest
```

#### Discussion

The system passes this type to the document provider app that the person selects to respond to the request.

## Topics

### Creating an identity document web presentment raw request
- [init(requestType: IdentityDocumentWebPresentmentRawRequest.RequestType, requestData: Data)](identitydocumentwebpresentmentrawrequest/init(requesttype:requestdata:).md)
  Initializes a web presentment raw request.
- [var requestData: Data](identitydocumentwebpresentmentrawrequest/requestdata.md)
  The request data blob for the web presentment raw request.
- [var requestType: IdentityDocumentWebPresentmentRawRequest.RequestType](identitydocumentwebpresentmentrawrequest/requesttype-swift.property.md)
  The request type for the current request that the system uses to help the document provider deserialize the request.
### Validating a web presentment raw request
- [struct IdentityDocumentWebPresentmentRawRequestValidator](identitydocumentwebpresentmentrawrequestvalidator.md)
  A type that contains functions for validating the incoming web presentment raw request.
### Enumerations
- [IdentityDocumentWebPresentmentRawRequest.RequestType](identitydocumentwebpresentmentrawrequest/requesttype-swift.enum.md)
  Defines the types of request formats supported by the system.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentwebpresentmentrawrequest)*