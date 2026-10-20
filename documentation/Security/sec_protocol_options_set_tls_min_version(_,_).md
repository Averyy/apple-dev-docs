# sec_protocol_options_set_tls_min_version(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 12.0+ - Deprecated in 13.0 (renamed: sec_protocol_options_set_min_tls_protocol_version(_:_:))
- iPadOS 12.0+ - Deprecated in 13.0 (renamed: sec_protocol_options_set_min_tls_protocol_version(_:_:))
- Mac Catalyst 12.0+ - Deprecated in 13.0 (renamed: sec_protocol_options_set_min_tls_protocol_version(_:_:))
- macOS 10.14+ - Deprecated in 10.15 (renamed: sec_protocol_options_set_min_tls_protocol_version(_:_:))
- tvOS 12.0+ - Deprecated in 13.0 (renamed: sec_protocol_options_set_min_tls_protocol_version(_:_:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: sec_protocol_options_set_min_tls_protocol_version(_:_:))
- watchOS 5.0+ - Deprecated in 6.0 (renamed: sec_protocol_options_set_min_tls_protocol_version(_:_:))

## Declaration

```swift
func sec_protocol_options_set_tls_min_version(_ options: sec_protocol_options_t, _ version: SSLProtocol)
```

```c
void sec_protocol_options_set_tls_min_version(sec_protocol_options_t options, SSLProtocol version);
```

#### Discussion

Set the minimum support TLS version.

## Parameters

- `options`: A `sec_protocol_options_t` instance.
- `version`: A SSLProtocol enum value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_options_set_tls_min_version(_:_:))*