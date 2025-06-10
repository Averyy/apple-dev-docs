# init(content:)

**Framework**: IdentityDocumentServicesUI  
**Kind**: init

Initialize an ISO 18013 mobile document raw request scene.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
@MainActor
@preconcurrency init(@ViewBuilder content: @escaping (ISO18013MobileDocumentRequestContext) -> Content)
```

## Parameters

- `content`: A closure that builds the authorization UI with the provided context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/iso18013mobiledocumentrequestscene/init(content:))*