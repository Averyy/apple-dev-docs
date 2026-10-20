# es_mute_path_prefix(_:_:)

**Framework**: Endpoint Security  
**Kind**: func  
**Role**: Function

Suppresses events from executables matching a path prefix.

**Availability**:
- macOS 10.15+ - Deprecated in 12.0

> **Deprecated**: Use [`es_mute_path(_:_:_:)`](./es_mute_path%28_,_,_%29.md) or [`es_mute_path_events(_:_:_:_:_:)`](./es_mute_path_events%28_,_,_,_,_%29.md) instead.

## Declaration

```swift
func es_mute_path_prefix(_ client: OpaquePointer, _ path_prefix: UnsafePointer<CChar>) -> es_return_t
```

```c
extern es_return_t es_mute_path_prefix(es_client_t *client, const char *path_prefix);
```

## Parameters

- `client`: The client for which to mute events.
- `path_prefix`: A prefix string. The client stops receiving events from executables whose paths begin with this string.

## See Also

### Deprecated Functions
- [func es_muted_processes(OpaquePointer, UnsafeMutablePointer<Int>, UnsafeMutablePointer<UnsafeMutablePointer<audit_token_t>>?) -> es_return_t](./es_muted_processes%28_,_,_%29.md)
  Generates a list of muted processes.
- [func es_mute_path_literal(OpaquePointer, UnsafePointer<CChar>) -> es_return_t](./es_mute_path_literal%28_,_%29.md)
  Suppresses events from executables matching a path literal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_mute_path_prefix(_:_:))*