# sec_certificate_copy_ref(_:)

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
func sec_certificate_copy_ref(_ certificate: sec_certificate_t) -> Unmanaged<SecCertificate>
```

```c
SecCertificateRefsec_certificate_copy_ref(sec_certificate_t certificate);
```

#### Return Value

The underlying `SecCertificateRef` instance.

#### Discussion

Copy a retained reference to the underlying `SecCertificateRef` instance.

## Parameters

- `certificate`: A `sec_certificate_t` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_certificate_copy_ref(_:))*