# sec_protocol_options_set_peer_authentication_required(_:_:)

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
func sec_protocol_options_set_peer_authentication_required(_ options: sec_protocol_options_t, _ peer_authentication_required: Bool)
```

#### Discussion

```None
 Enable or disable peer authentication. Clients default to true, whereas servers default to false.
```

## Parameters

- `options`: A   instance.
- `peer_authentication_required`: Flag to enable or disable mandatory peer authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_options_set_peer_authentication_required(_:_:))*