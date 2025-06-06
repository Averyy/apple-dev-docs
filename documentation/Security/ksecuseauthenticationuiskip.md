# kSecUseAuthenticationUISkip

**Framework**: Security  
**Kind**: var

A value that indicates items requiring user authentication should be skipped.

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
let kSecUseAuthenticationUISkip: CFString
```

#### Discussion

Silently skip any items that require user authentication. Only use this value with the [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecuseauthenticationuiskip)*