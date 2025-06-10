# sec_trust_create(_:)

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
func sec_trust_create(_ trust: SecTrust) -> sec_trust_t?
```

#### Return Value

A `sec_trust_t` instance.

#### Discussion

```None
 Create an ARC-able `sec_trust_t` instance from a `SecTrustRef`.
```

## Parameters

- `trust`: A   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_trust_create(_:))*