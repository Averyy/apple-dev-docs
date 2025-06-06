# SecCertificateCopyPublicKey(_:)

**Framework**: Security  
**Kind**: func

Retrieves the public key from a certificate.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- macOS 10.3+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
func SecCertificateCopyPublicKey(_ certificate: SecCertificate) -> SecKey?
```

## Mentions

- [Examining a Certificate](examining-a-certificate.md)

#### Return Value

In iOS, the certificate’s public key.

#### Discussion

In macOS, a result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `certificate`: The certificate object from which to retrieve the public key.
- `key`: In macOS, points to the public key for the specified certificate. In Objective-C, call the   function to release this object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificatecopypublickey(_:_:))*