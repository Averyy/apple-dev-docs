# sec_trust_copy_ref(_:)

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
func sec_trust_copy_ref(_ trust: sec_trust_t) -> Unmanaged<SecTrust>
```

#### Return Value

The underlying `SecTrustRef` instance.

#### Discussion

```None
  Copy a retained reference to the underlying `SecTrustRef` instance.
```

## Parameters

- `trust`: A   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_trust_copy_ref(_:))*