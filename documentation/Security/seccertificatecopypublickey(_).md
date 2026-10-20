# SecCertificateCopyPublicKey(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the public key from a certificate.

**Availability**:
- iOS 10.3+ - Deprecated in 12.0 (renamed: SecCertificateCopyKey(_:))
- iPadOS 10.3+ - Deprecated in 12.0 (renamed: SecCertificateCopyKey(_:))
- Mac Catalyst 10.3+ - Deprecated in 12.0 (renamed: SecCertificateCopyKey(_:))
- macOS 10.3+ - Deprecated in 10.14 (renamed: SecCertificateCopyKey(_:))
- tvOS 10.2+ - Deprecated in 12.0 (renamed: SecCertificateCopyKey(_:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: SecCertificateCopyKey(_:))
- watchOS 3.2+ - Deprecated in 5.0 (renamed: SecCertificateCopyKey(_:))

> **Deprecated**: Use [`SecCertificateCopyKey(_:)`](./seccertificatecopykey%28_%29.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
func SecCertificateCopyPublicKey(_ certificate: SecCertificate) -> SecKey?
```

*macOS*

```swift
func SecCertificateCopyPublicKey(_ certificate: SecCertificate, _ key: UnsafeMutablePointer<SecKey?>) -> OSStatus
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```c
SecKeyRefSecCertificateCopyPublicKey(SecCertificateRef certificate);
```

*macOS*

```c
OSStatus SecCertificateCopyPublicKey(SecCertificateRef certificate, SecKeyRef*key);
```

## Mentions

- [Examining a Certificate](./examining-a-certificate.md)

#### Return Value

In iOS, the certificate’s public key.

#### Discussion

In macOS, a result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Parameters

- `certificate`: The certificate object from which to retrieve the public key.
- `key`: In macOS, points to the public key for the specified certificate. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificatecopypublickey(_:))*