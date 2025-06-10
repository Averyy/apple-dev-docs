# validateISO18013MobileDocumentRequest(_:origin:)

**Framework**: IdentityDocumentServices  
**Kind**: method

Validates an incoming raw ISO 18013-5 request.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
func validateISO18013MobileDocumentRequest(_ requestData: Data, origin: URL) throws -> ISO18013MobileDocumentRequest
```

#### Return Value

A validated and parsed ISO 18013-5 mobile document request.

## Parameters

- `requestData`: The incoming raw ISO 18013-5 request.
- `origin`: The origin of the requesting website.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentwebpresentmentrawrequestvalidator/validateiso18013mobiledocumentrequest(_:origin:))*