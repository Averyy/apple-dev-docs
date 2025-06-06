# kSecTrustCertificateTransparencyWhiteList

**Framework**: Security  
**Kind**: var

A key whose value is a Boolean used to indicate the chain satisfies Certificate Transparency by being on the allow list.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
let kSecTrustCertificateTransparencyWhiteList: CFString
```

#### Discussion

When the key is present and the value set to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue), it indicates the chain is Extended Validation (EV) and not Certificate Transparency (CT) qualified, but is nonetheless included on the allow list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectrustcertificatetransparencywhitelist)*