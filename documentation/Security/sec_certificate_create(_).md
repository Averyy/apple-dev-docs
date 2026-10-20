# sec_certificate_create(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

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
func sec_certificate_create(_ certificate: SecCertificate) -> sec_certificate_t?
```

```c
sec_certificate_tsec_certificate_create(SecCertificateRef certificate);
```

#### Return Value

A `sec_certificate_t` instance.

#### Discussion

Create an ARC-able `sec_certificate_t` instance from a `SecCertificateRef`.

## Parameters

- `certificate`: A `SecCertificateRef` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_certificate_create(_:))*