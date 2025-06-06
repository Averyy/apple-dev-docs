# SecTrustResultType.confirm

**Framework**: Security  
**Kind**: case

User confirmation is required before proceeding.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case confirm
```

#### Discussion

This value indicates that the user previously chose to always be asked for permission before accepting one of the certificates in the chain. The Keychain Access utility refers to this value as “Ask Permission.” This return value is no longer used, but may occur in older versions of macOS.

Either ask the user what to do or reject the certificate. If you ask the user what to do in macOS, use an instance of the [`SFCertificateTrustPanel`](https://developer.apple.com/documentation/SecurityInterface/SFCertificateTrustPanel) class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustresulttype/confirm)*