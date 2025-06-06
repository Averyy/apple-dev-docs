# kSecUseAuthenticationUIFail

**Framework**: Security  
**Kind**: var

A value that indicates user authentication is disallowed.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecUseAuthenticationUIFail: CFString
```

#### Discussion

When you specify this value, if user authentication is needed, the function returns the [`errSecInteractionNotAllowed`](errsecinteractionnotallowed.md) error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecuseauthenticationuifail)*