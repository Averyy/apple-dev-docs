# sendResponse(_:)

**Framework**: IdentityDocumentServicesUI  
**Kind**: method

Builds and sends an ISO 18013 mobile document response.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
func sendResponse(_ responseHandler: @escaping (IdentityDocumentWebPresentmentRawRequest) async throws -> ISO18013MobileDocumentResponse) async throws
```

## Parameters

- `responseHandler`: A handler you use to build the response. This handler provides the raw web presentment request, and returns the ISO 18013 mobile document response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/iso18013mobiledocumentrequestcontext/sendresponse(_:))*