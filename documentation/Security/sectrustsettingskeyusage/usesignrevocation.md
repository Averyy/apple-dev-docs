# useSignRevocation

**Framework**: Security  
**Kind**: property

The key can be used to sign an OCSP (online certificate status protocol) message or CRL (certificate verification list), or to verify a signature.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var useSignRevocation: SecTrustSettingsKeyUsage { get }
```

#### Discussion

OCSP messages and CRLs are used to revoke certificates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustsettingskeyusage/usesignrevocation)*