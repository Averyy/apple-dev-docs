# sec_protocol_metadata_copy_server_name(_:)

**Framework**: Security  
**Kind**: func

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```swift
func sec_protocol_metadata_copy_server_name(_ metadata: sec_protocol_metadata_t) -> UnsafePointer<CChar>?
```

#### Return Value

Returns A NULL-terminated string carrying the server name, or NULL if none was provided.

#### Discussion

```None
 Obtain a copy of the server name offered by a client or server during
 connection establishmet. This is the value commonly carried
 in the TLS SNI extesion. The caller is expected to `free` the output
 string when it is no longer needed.
```

## Parameters

- `metadata`: A   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_metadata_copy_server_name(_:))*