# kSecMatchIssuers

**Framework**: Security  
**Kind**: var

A key whose value is a string to match against a certificate or identity’s issuers.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecMatchIssuers: CFString
```

#### Discussion

The corresponding value is of type [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray), where the array consists of X.500 names of type [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData). If provided, returned certificates or identities are limited to those whose certificate chain contains one of the issuers provided in this list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecmatchissuers)*