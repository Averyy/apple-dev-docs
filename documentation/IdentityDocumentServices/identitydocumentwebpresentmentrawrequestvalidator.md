# IdentityDocumentWebPresentmentRawRequestValidator

**Framework**: IdentityDocumentServices  
**Kind**: struct

A type that contains functions for validating the incoming web presentment raw request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
struct IdentityDocumentWebPresentmentRawRequestValidator
```

## Topics

### Initializers
- [init()](identitydocumentwebpresentmentrawrequestvalidator/init.md)
  Initializes a raw request validator.
### Instance Methods
- [func validateISO18013MobileDocumentRequest(Data, origin: URL) throws -> ISO18013MobileDocumentRequest](identitydocumentwebpresentmentrawrequestvalidator/validateiso18013mobiledocumentrequest(_:origin:).md)
  Validates an incoming raw ISO 18013-5 request.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentwebpresentmentrawrequestvalidator)*