# presentmentRequests

**Framework**: IdentityDocumentServices  
**Kind**: property

An array of the presentment requests that exist in the incoming mobile document request.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
var presentmentRequests: [ISO18013MobileDocumentRequest.PresentmentRequest]
```

#### Discussion

> **Note**:  You must return all presentment requests marked as mandatory in order to complete the mobile document request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/iso18013mobiledocumentrequest/presentmentrequests)*