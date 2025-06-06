# SecTrustSettingsRemoveTrustSettings(_:_:)

**Framework**: Security  
**Kind**: func

Deletes the trust settings for a certificate.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecTrustSettingsRemoveTrustSettings(_ certRef: SecCertificate, _ domain: SecTrustSettingsDomain) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md). Returns [`errSecItemNotFound`](errsecitemnotfound.md) if no trust settings exist for the certificate.

#### Discussion

If a certificate has no trust settings, the certificate must be verified to a known, trusted certificate.

## Parameters

- `certRef`: The certificate whose trust settings you wish to remove. Pass the value   to remove the default root certificate trust settings for the domain.
- `domain`: The trust settings domain for which you wish to remove the trust settings. For possible values, see  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustsettingsremovetrustsettings(_:_:))*