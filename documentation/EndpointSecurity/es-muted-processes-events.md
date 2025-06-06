# es_muted_processes_events(_:_:)

**Framework**: Endpoint Security  
**Kind**: func

Retrieve a list of all muted processes.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func es_muted_processes_events(_ client: OpaquePointer, _ muted_processes: UnsafeMutablePointer<UnsafeMutablePointer<es_muted_processes_t>?>) -> es_return_t
```

#### Return Value

A value that indicates whether the request for muted processes succeeded or failed with an error.

## Parameters

- `client`: A previously-created client. If the call succeeds, the   structure contains processes muted for this client.
- `muted_processes`: On output, a structure that contains the muted processes. You must dispose of this memory by calling  .

## See Also

- [func es_mute_process(OpaquePointer, UnsafePointer<audit_token_t>) -> es_return_t](es_mute_process(_:_:).md)
  Suppresses events from a given process.
- [func es_mute_process_events(OpaquePointer, UnsafePointer<audit_token_t>, UnsafePointer<es_event_type_t>, Int) -> es_return_t](es_mute_process_events(_:_:_:_:).md)
  Suppresses a subset of events from a given process.
- [struct es_muted_processes_t](es_muted_processes_t.md)
  A structure for a set of muted processes.
- [func es_release_muted_processes(UnsafeMutablePointer<es_muted_processes_t>)](es_release_muted_processes(_:).md)
  Frees resources associated with a set of previously-retrieved muted processes.
- [func es_mute_path(OpaquePointer, UnsafePointer<CChar>, es_mute_path_type_t) -> es_return_t](es_mute_path(_:_:_:).md)
  Suppresses events from executables that match a given path.
- [func es_mute_path_events(OpaquePointer, UnsafePointer<CChar>, es_mute_path_type_t, UnsafePointer<es_event_type_t>, Int) -> es_return_t](es_mute_path_events(_:_:_:_:_:).md)
  Suppresses a subset of events from executables that match a given path.
- [struct es_mute_path_type_t](es_mute_path_type_t.md)
  The type of a path argument, such as a prefix or a path literal.
- [func es_muted_paths_events(OpaquePointer, UnsafeMutablePointer<UnsafeMutablePointer<es_muted_paths_t>>?) -> es_return_t](es_muted_paths_events(_:_:).md)
  Retrieve a list of all muted paths.
- [struct es_muted_paths_t](es_muted_paths_t.md)
  A structure for a set of muted paths.
- [func es_release_muted_paths(UnsafeMutablePointer<es_muted_paths_t>)](es_release_muted_paths(_:).md)
  Frees resources associated with a set of previously-retrieved muted paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_muted_processes_events(_:_:))*