# sec_protocol_options_set_local_identity(_:_:)

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
func sec_protocol_options_set_local_identity(_ options: sec_protocol_options_t, _ identity: sec_identity_t)
```

#### Discussion

Set the local identity to be used for this protocol instance.

## Parameters

- `options`: A   instance.
- `identity`: A   instance carrying the private key and certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_options_set_local_identity(_:_:))*