# sec_identity_copy_certificates_ref(_:)

**Framework**: Security  
**Kind**: func

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
func sec_identity_copy_certificates_ref(_ identity: sec_identity_t) -> Unmanaged<CFArray>?
```

#### Return Value

The underlying `CFArrayRef` container with `SecCertificateRef` instances.

#### Discussion

```None
 Copy a retained reference to the underlying `CFArrayRef` container of `SecCertificateRef` types.
```

## Parameters

- `identity`: A   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_identity_copy_certificates_ref(_:))*