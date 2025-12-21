# sec_identity_copy_ref(_:)

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
func sec_identity_copy_ref(_ identity: sec_identity_t) -> Unmanaged<SecIdentity>?
```

#### Return Value

The underlying `SecIdentityRef` instance.

#### Discussion

Copy a retained reference to the underlying `SecIdentityRef` instance.

## Parameters

- `identity`: A   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_identity_copy_ref(_:))*