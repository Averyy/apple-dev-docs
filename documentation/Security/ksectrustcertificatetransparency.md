# kSecTrustCertificateTransparency

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a Boolean used to indicate Certificate Transparency.

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
let kSecTrustCertificateTransparency: CFString
```

```c
extern CFStringRef const kSecTrustCertificateTransparency;
```

#### Discussion

When the key is present and the value set to [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md), it indicates the chain is Certificate Transparency (CT) qualified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectrustcertificatetransparency)*