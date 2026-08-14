# SecTrustSettingsCopyCertificates(_:_:)

**Framework**: Security  
**Kind**: func

Obtains an array of all certificates that have trust settings in a specific trust settings domain.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecTrustSettingsCopyCertificates(_ domain: SecTrustSettingsDomain, _ certArray: UnsafeMutablePointer<CFArray?>?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md). Returns [`errSecNoTrustSettings`](errsecnotrustsettings.md) if no trust settings exist for the specified domain.

## Parameters

- `domain`: The trust settings domain for which you want a list of certificates. For possible values, see [`SecTrustSettingsDomain`](sectrustsettingsdomain.md).
- `certArray`: On return, an array of `SecCertificateRef` objects representing the certificates that have trust settings in the specified domain. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/cfrelease) function to release this object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustsettingscopycertificates(_:_:))*