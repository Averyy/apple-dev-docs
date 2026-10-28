# kSecUseAuthenticationUIAllow

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A value that indicates user authentication is allowed.

**Availability**:
- iOS 9.0+ - Deprecated in 14.0
- iPadOS 9.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.11+ - Deprecated in 11.0
- tvOS 9.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 7.0

> **Deprecated**: Instead of kSecUseAuthenticationUI, use kSecUseAuthenticationContext and set LAContext.interactionNotAllowed property

## Declaration

```swift
let kSecUseAuthenticationUIAllow: CFString
```

```c
extern CFStringRef const kSecUseAuthenticationUIAllow;
```

## Discussion

The user may be prompted for authentication. This is the default value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecuseauthenticationuiallow)*