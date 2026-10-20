# es_mute_path_prefix(_:_:)

**Framework**: Endpoint Security  
**Kind**: func

Suppresses events from executables matching a path prefix.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func es_mute_path_prefix(_ client: OpaquePointer, _ path_prefix: UnsafePointer<CChar>) -> es_return_t
```

## Parameters

- `client`: The client for which to mute events.
- `path_prefix`: A prefix string. The client stops receiving events from executables whose paths begin with this string.

## See Also

- [func es_muted_processes(OpaquePointer, UnsafeMutablePointer<Int>, UnsafeMutablePointer<UnsafeMutablePointer<audit_token_t>>?) -> es_return_t](es_muted_processes(_:_:_:).md)
  Generates a list of muted processes.
- [func es_mute_path_literal(OpaquePointer, UnsafePointer<CChar>) -> es_return_t](es_mute_path_literal(_:_:).md)
  Suppresses events from executables matching a path literal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_mute_path_prefix(_:_:))*