# SecTrustSettingsResult.trustRoot

**Framework**: Security  
**Kind**: case

This root certificate is explicitly trusted.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
case trustRoot
```

#### Discussion

If the certificate is not a root (self-signed) certificate, the usage constraints dictionary is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustsettingsresult/trustroot)*