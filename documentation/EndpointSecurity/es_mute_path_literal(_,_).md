# es_mute_path_literal(_:_:)

**Framework**: Endpoint Security  
**Kind**: func  
**Role**: Function

Suppresses events from executables matching a path literal.

**Availability**:
- macOS 10.15+ - Deprecated in 12.0

> **Deprecated**: Use [`es_mute_path(_:_:_:)`](./es_mute_path%28_,_,_%29.md) or [`es_mute_path_events(_:_:_:_:_:)`](./es_mute_path_events%28_,_,_,_,_%29.md) instead.

## Declaration

```swift
func es_mute_path_literal(_ client: OpaquePointer, _ path_literal: UnsafePointer<CChar>) -> es_return_t
```

```c
extern es_return_t es_mute_path_literal(es_client_t *client, const char *path_literal);
```

## Parameters

- `client`: The client for which to mute events.
- `path_literal`: The path against which suppressed executables must match exactly.

## See Also

### Deprecated Functions
- [func es_muted_processes(OpaquePointer, UnsafeMutablePointer<Int>, UnsafeMutablePointer<UnsafeMutablePointer<audit_token_t>>?) -> es_return_t](./es_muted_processes%28_,_,_%29.md)
  Generates a list of muted processes.
- [func es_mute_path_prefix(OpaquePointer, UnsafePointer<CChar>) -> es_return_t](./es_mute_path_prefix%28_,_%29.md)
  Suppresses events from executables matching a path prefix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_mute_path_literal(_:_:))*