# kSecTrustCertificateTransparencyWhiteList

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a Boolean used to indicate the chain satisfies Certificate Transparency by being on the allow list.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.13
- tvOS 10.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 4.0

## Declaration

```swift
let kSecTrustCertificateTransparencyWhiteList: CFString
```

```c
extern CFStringRef const kSecTrustCertificateTransparencyWhiteList;
```

## Discussion

When the key is present and the value set to [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md), it indicates the chain is Extended Validation (EV) and not Certificate Transparency (CT) qualified, but is nonetheless included on the allow list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectrustcertificatetransparencywhitelist)*