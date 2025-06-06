# invalidate()

**Framework**: SecureElementCredential  
**Kind**: method

Invalidates the configuration and transitions the underlying session state to management.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func invalidate() async throws
```

#### Discussion

Call `invalidate()` in the closure passed to doc://com.apple.documentation/documentation/SwiftUI/View/transactionTask(_:action) when you complete your wired transaction or card emulation. Your app is responsible for invalidating any wired or card emulation state by calling this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialtransaction/configuration/invalidate())*