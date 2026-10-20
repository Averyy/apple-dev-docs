# PKCS1

**Framework**: Security  
**Kind**: property  
**Role**: Type Property

PKCS1 padding.

**Availability**:
- iOS 2.0+ - Deprecated in 15.0
- iPadOS 2.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.6+ - Deprecated in 12.0
- tvOS 4.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 8.0

> **Deprecated**: Replaced with SecKeyAlgorithm

## Declaration

```swift
static var PKCS1: SecPadding { get }
```

```c
kSecPaddingPKCS1
```

#### Discussion

For elliptic curve, defaults to a signature in x9.62 DER encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpadding/pkcs1)*