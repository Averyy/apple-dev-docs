# kSecUseAuthenticationUI

**Framework**: Security  
**Kind**: var

A key whose value indicates whether the user is prompted for authentication.

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
let kSecUseAuthenticationUI: CFString
```

#### Discussion

The corresponding value is of type [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) and contains one of the values listed in [`UI authentication values`](search-attribute-keys-and-values#UI-authentication-values.md). The value specifies whether or not the user is prompted for authentication, if needed. A default value of [`kSecUseAuthenticationUIAllow`](ksecuseauthenticationuiallow.md) is assumed when this key is not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecuseauthenticationui)*