# kSecAttrIssuer

**Framework**: Security  
**Kind**: var

A key whose value indicates the item’s issuer.

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
let kSecAttrIssuer: CFString
```

#### Discussion

The corresponding value is of type [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) and contains the X.500 issuer name of a certificate. Items of class [`kSecClassCertificate`](ksecclasscertificate.md) have this attribute. Read only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrissuer)*