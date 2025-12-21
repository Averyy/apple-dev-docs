# sec_identity_create_with_certificates(_:_:)

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
func sec_identity_create_with_certificates(_ identity: SecIdentity, _ certificates: CFArray) -> sec_identity_t?
```

#### Return Value

A `sec_identity_t` instance.

#### Discussion

Create an ARC-able `sec_identity_t` instance from a `SecIdentityRef` and array of SecCertificateRef instances.

## Parameters

- `identity`: A   instance.
- `certificates`: An array of   instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_identity_create_with_certificates(_:_:))*