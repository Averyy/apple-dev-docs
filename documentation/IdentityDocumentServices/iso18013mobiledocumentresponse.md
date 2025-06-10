# ISO18013MobileDocumentResponse

**Framework**: IdentityDocumentServices  
**Kind**: struct

A type representing the document response from a web presentment request.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
struct ISO18013MobileDocumentResponse
```

## Topics

### Initializers
- [init(responseData: Data)](iso18013mobiledocumentresponse/init(responsedata:).md)
  Create an ISO 18013 mobile document response.
### Instance Properties
- [let responseData: Data](iso18013mobiledocumentresponse/responsedata.md)
  The presentment response data that has a format based on request type.

## Relationships

### Conforms To
- [IdentityDocumentWebPresentmentResponse](identitydocumentwebpresentmentresponse.md)
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
- [struct IdentityDocumentWebPresentmentRawRequest](identitydocumentwebpresentmentrawrequest.md)
  A struct that defines the type that represents a raw web presentment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/iso18013mobiledocumentresponse)*