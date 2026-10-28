# sec_protocol_metadata_get_server_name(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 12.0+ - Deprecated in 18.5 (renamed: sec_protocol_metadata_copy_server_name(_:))
- iPadOS 12.0+ - Deprecated in 18.5 (renamed: sec_protocol_metadata_copy_server_name(_:))
- Mac Catalyst 13.1+ - Deprecated in 18.5 (renamed: sec_protocol_metadata_copy_server_name(_:))
- macOS 10.14+ - Deprecated in 15.5 (renamed: sec_protocol_metadata_copy_server_name(_:))
- tvOS 12.0+ - Deprecated in 18.5 (renamed: sec_protocol_metadata_copy_server_name(_:))
- visionOS 1.0+ - Deprecated in 2.5 (renamed: sec_protocol_metadata_copy_server_name(_:))
- watchOS 5.0+ - Deprecated in 11.5 (renamed: sec_protocol_metadata_copy_server_name(_:))

## Declaration

```swift
func sec_protocol_metadata_get_server_name(_ metadata: sec_protocol_metadata_t) -> UnsafePointer<CChar>?
```

```c
const char *sec_protocol_metadata_get_server_name(sec_protocol_metadata_t metadata);
```

## Return Value

Returns A NULL-terminated string carrying the server name, or NULL if none was provided.

## Discussion

Obtain the server name offered by a client or server during connection establishmet. This is the value commonly carried in the TLS SNI extesion.

## Parameters

- `metadata`: A `sec_protocol_metadata_t` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_metadata_get_server_name(_:))*