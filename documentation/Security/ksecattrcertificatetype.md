# kSecAttrCertificateType

**Framework**: Security  
**Kind**: var

A key whose value indicates the item’s certificate type.

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
let kSecAttrCertificateType: CFString
```

#### Discussion

The corresponding value is of type [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) and denotes the certificate type (see the `CSSM_CERT_TYPE` enumeration in cssmtype.h). Items of class [`kSecClassCertificate`](ksecclasscertificate.md) have this attribute. Read only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrcertificatetype)*