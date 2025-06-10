# sec_identity_access_certificates(_:_:)

**Framework**: Security  
**Kind**: func

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func sec_identity_access_certificates(_ identity: sec_identity_t, _ handler: @escaping (sec_certificate_t) -> Void) -> Bool
```

#### Return Value

Returns true if the peer certificates were accessible, false otherwise.

#### Discussion

```None
 Access the certificates associated with the `sec_identity_t` instance.
```

## Parameters

- `identity`: A   instance.
- `handler`: A block to invoke one or more times with   instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_identity_access_certificates(_:_:))*