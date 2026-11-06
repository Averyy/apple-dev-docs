# init(content:)

**Framework**: IdentityDocumentServicesUI  
**Kind**: init  
**Role**: Initializer

Creates a request scene for handling a full OpenID4VP mobile document raw request.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst

## Declaration

```swift
@MainActor
@preconcurrency init(@ViewBuilder content: @escaping (OpenID4VPRawRequestContext) -> Content)
```

## Parameters

- `content`: A closure that builds the authorization UI. The closure receives an [`OpenID4VPRawRequestContext`](../openid4vprawrequestcontext.md) that contains the request and the functions you use to respond to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservicesui/openid4vprawrequestscene/init(content:))*