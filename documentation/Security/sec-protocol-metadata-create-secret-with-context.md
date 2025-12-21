# sec_protocol_metadata_create_secret_with_context(_:_:_:_:_:_:)

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
func sec_protocol_metadata_create_secret_with_context(_ metadata: sec_protocol_metadata_t, _ label_len: Int, _ label: UnsafePointer<CChar>, _ context_len: Int, _ context: UnsafePointer<UInt8>, _ exporter_length: Int) -> dispatch_data_t?
```

#### Return Value

Returns a dispatch_data_t object carrying the exported secret.

#### Discussion

Export a secret, e.g., a cryptographic key, derived from the protocol metadata using a label and context string.

## Parameters

- `metadata`: A   instance.
- `label_len`: Length of the KDF label string.
- `label`: KDF label string.
- `context_len`: Length of the KDF context string.
- `context`: Constant opaque context value
- `exporter_length`: Length of the secret to be exported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_metadata_create_secret_with_context(_:_:_:_:_:_:))*