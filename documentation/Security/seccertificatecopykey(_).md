# SecCertificateCopyKey(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the public key for a given certificate.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func SecCertificateCopyKey(_ certificate: SecCertificate) -> SecKey?
```

```c
SecKeyRefSecCertificateCopyKey(SecCertificateRef certificate);
```

#### Return Value

The public key. In Objective-C, free this key with a call to the [`CFRelease`](../CoreFoundation/cfrelease.md) function when you are done with it.

#### Discussion

The return reference is `NULL` if the public key has an encoding issue or uses an unsupported algorithm.

## Parameters

- `certificate`: The certificate from which to copy the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificatecopykey(_:))*