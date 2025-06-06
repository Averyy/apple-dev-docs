# sec_protocol_metadata_access_peer_certificate_chain(_:_:)

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
func sec_protocol_metadata_access_peer_certificate_chain(_ metadata: sec_protocol_metadata_t, _ handler: @escaping (sec_certificate_t) -> Void) -> Bool
```

#### Return Value

Returns true if the peer certificates were accessible, false otherwise.

#### Discussion

```None
  Get the certificate chain of the protocol instance peer.
```

## Parameters

- `metadata`: A   instance.
- `handler`: A block to invoke one or more times with sec_certificate_t objects


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_metadata_access_peer_certificate_chain(_:_:))*