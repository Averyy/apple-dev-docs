# performRequests(_:origin:)

**Framework**: IdentityDocumentServicesUI  
**Kind**: method

Performs an identity document request.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
final func performRequests(_ requests: [any IdentityDocumentWebPresentmentRequest], origin: URL) async throws -> any IdentityDocumentWebPresentmentResponse
```

#### Return Value

A response that contains the requested document information.

#### Discussion

In iOS, the systems sources this document from a document provider installed on the current device. On other platforms, this function triggers a remote presentment flow where the app prompts the person to use a nearby device for the presentment.

## Parameters

- `requests`: A list of incoming document requests.
- `origin`: The origin of the requesting website.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentwebpresentmentcontroller/performrequests(_:origin:))*