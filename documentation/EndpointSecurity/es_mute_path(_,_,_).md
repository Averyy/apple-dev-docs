# es_mute_path(_:_:_:)

**Framework**: Endpoint Security  
**Kind**: func  
**Role**: Function

Suppresses events from executables that match a given path.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func es_mute_path(_ client: OpaquePointer, _ path: UnsafePointer<CChar>, _ type: es_mute_path_type_t) -> es_return_t
```

```c
extern es_return_t es_mute_path(es_client_t *client, const char *path, es_mute_path_type_t type);
```

## Return Value

A value that indicates whether the mute request succeeded or failed with an error.

## Discussion

To mute a subset of events from a path, use [`es_mute_path_events(_:_:_:_:_:)`](./es_mute_path_events%28_,_,_,_,_%29.md).

## Parameters

- `client`: A previously-created client. If the call succeeds, this client no longer receives events from executables whose paths match `path`.
- `path`: The path to mute. The client stops receiving events from executables whose paths match this string.
- `type`: The type of the `path` argument, either a prefix or a literal path.

## See Also

### Muting Events
- [func es_mute_process(OpaquePointer, UnsafePointer<audit_token_t>) -> es_return_t](./es_mute_process%28_,_%29.md)
  Suppresses events from a given process.
- [func es_mute_process_events(OpaquePointer, UnsafePointer<audit_token_t>, UnsafePointer<es_event_type_t>, Int) -> es_return_t](./es_mute_process_events%28_,_,_,_%29.md)
  Suppresses a subset of events from a given process.
- [struct es_muted_processes_t](./es_muted_processes_t.md)
  A structure for a set of muted processes.
- [func es_release_muted_processes(UnsafeMutablePointer<es_muted_processes_t>)](./es_release_muted_processes%28_%29.md)
  Frees resources associated with a set of previously-retrieved muted processes.
- [func es_muted_processes_events(OpaquePointer, UnsafeMutablePointer<UnsafeMutablePointer<es_muted_processes_t>?>) -> es_return_t](./es_muted_processes_events%28_,_%29.md)
  Retrieve a list of all muted processes.
- [func es_mute_path_events(OpaquePointer, UnsafePointer<CChar>, es_mute_path_type_t, UnsafePointer<es_event_type_t>, Int) -> es_return_t](./es_mute_path_events%28_,_,_,_,_%29.md)
  Suppresses a subset of events from executables that match a given path.
- [struct es_mute_path_type_t](./es_mute_path_type_t.md)
  The type of a path argument, such as a prefix or a path literal.
- [func es_muted_paths_events(OpaquePointer, UnsafeMutablePointer<UnsafeMutablePointer<es_muted_paths_t>>?) -> es_return_t](./es_muted_paths_events%28_,_%29.md)
  Retrieve a list of all muted paths.
- [struct es_muted_paths_t](./es_muted_paths_t.md)
  A structure for a set of muted paths.
- [func es_release_muted_paths(UnsafeMutablePointer<es_muted_paths_t>)](./es_release_muted_paths%28_%29.md)
  Frees resources associated with a set of previously-retrieved muted paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_mute_path(_:_:_:))*