# SecIdentityCreate(_:_:_:)

**Framework**: Security  
**Kind**: func

**Availability**:
- iOS 11.2+
- iPadOS 11.2+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.2+
- visionOS 1.0+
- watchOS 4.2+

## Declaration

```swift
func SecIdentityCreate(_ allocator: CFAllocator?, _ certificate: SecCertificate, _ privateKey: SecKey) -> SecIdentity?
```

#### Return Value

An identity reference.

#### Discussion

Create a new identity object from the provided certificate and its associated private key.

This interface returns null if the private does not key correspond to the public key in the certifcate.

## Parameters

- `allocator`: CFAllocator to allocate the identity object. Pass NULL to use the default allocator.
- `certificate`: A certificate reference.
- `privateKey`: A private key reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secidentitycreate(_:_:_:))*