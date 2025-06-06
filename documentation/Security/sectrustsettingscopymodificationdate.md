# SecTrustSettingsCopyModificationDate(_:_:_:)

**Framework**: Security  
**Kind**: func

Obtains the date and time at which a certificate’s trust settings were last modified.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecTrustSettingsCopyModificationDate(_ certRef: SecCertificate, _ domain: SecTrustSettingsDomain, _ modificationDate: UnsafeMutablePointer<CFDate?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md). Returns [`errSecItemNotFound`](errsecitemnotfound.md) if no trust settings exist for the specified certificate and domain.

## Parameters

- `certRef`: The certificate for which you wish to obtain the modification time. Pass the value   to obtain the modification time for the default root certificate trust settings for the domain.
- `domain`: The trust settings domain of the trust settings for which you wish to obtain the modification time (it’s possible for a single certificate to have trust settings in more than one domain). For possible values, see  .
- `modificationDate`: On return, the date and time at which the certificate’s trust settings were last modified. In Objective-C, call the   function to release this object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustsettingscopymodificationdate(_:_:_:))*