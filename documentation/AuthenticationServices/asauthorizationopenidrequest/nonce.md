# nonce

**Framework**: Authentication Services  
**Kind**: property

A string value to pass to the identity provider.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var nonce: String? { get set }
```

#### Discussion

You can verify this value with the identity token provided as part of a successful ASAuthorization response.

The nonce size may depend on the actual technology used, and an error might be returned by the request execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationopenidrequest/nonce)*