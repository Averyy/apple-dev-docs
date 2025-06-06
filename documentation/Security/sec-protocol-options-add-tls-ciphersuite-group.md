# sec_protocol_options_add_tls_ciphersuite_group(_:_:)

**Framework**: Security  
**Kind**: func

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func sec_protocol_options_add_tls_ciphersuite_group(_ options: sec_protocol_options_t, _ group: SSLCiphersuiteGroup)
```

#### Discussion

```None
  Add a TLS ciphersuite group to the set of enabled ciphersuites.
```

## Parameters

- `options`: A   instance.
- `group`: A SSLCipherSuiteGroup value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_options_add_tls_ciphersuite_group(_:_:))*