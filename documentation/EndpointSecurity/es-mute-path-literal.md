# es_mute_path_literal(_:_:)

**Framework**: Endpoint Security  
**Kind**: func

Suppresses events from executables matching a path literal.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func es_mute_path_literal(_ client: OpaquePointer, _ path_literal: UnsafePointer<CChar>) -> es_return_t
```

## Parameters

- `client`: The client for which to mute events.
- `path_literal`: The path against which suppressed executables must match exactly.

## See Also

- [func es_muted_processes(OpaquePointer, UnsafeMutablePointer<Int>, UnsafeMutablePointer<UnsafeMutablePointer<audit_token_t>>?) -> es_return_t](es_muted_processes(_:_:_:).md)
  Generates a list of muted processes.
- [func es_mute_path_prefix(OpaquePointer, UnsafePointer<CChar>) -> es_return_t](es_mute_path_prefix(_:_:).md)
  Suppresses events from executables matching a path prefix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_mute_path_literal(_:_:))*