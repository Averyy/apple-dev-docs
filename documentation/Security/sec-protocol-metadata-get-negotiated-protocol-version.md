# sec_protocol_metadata_get_negotiated_protocol_version(_:)

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
func sec_protocol_metadata_get_negotiated_protocol_version(_ metadata: sec_protocol_metadata_t) -> SSLProtocol
```

#### Return Value

A SSLProtocol enum of the TLS version.

#### Discussion

```None
 Get the negotiated TLS version.
```

## Parameters

- `metadata`: A   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_metadata_get_negotiated_protocol_version(_:))*