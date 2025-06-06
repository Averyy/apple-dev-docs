# es_muted_paths_t

**Framework**: Endpoint Security  
**Kind**: struct

A structure for a set of muted paths.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_muted_paths_t
```

## Topics

### Accessing Muted Paths
- [var paths: UnsafePointer<es_muted_path_t>!](es_muted_paths_t/paths.md)
  An array containing the muted paths.
- [struct es_muted_path_t](es_muted_path_t.md)
  A structure that describes a path’s muted events.
- [var count: Int](es_muted_paths_t/count.md)
  The number of elements in the paths array.
### Initializers
- [init()](es_muted_paths_t/init.md)
- [init(count: Int, paths: UnsafePointer<es_muted_path_t>!)](es_muted_paths_t/init(count:paths:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func es_mute_process(OpaquePointer, UnsafePointer<audit_token_t>) -> es_return_t](es_mute_process(_:_:).md)
  Suppresses events from a given process.
- [func es_mute_process_events(OpaquePointer, UnsafePointer<audit_token_t>, UnsafePointer<es_event_type_t>, Int) -> es_return_t](es_mute_process_events(_:_:_:_:).md)
  Suppresses a subset of events from a given process.
- [struct es_muted_processes_t](es_muted_processes_t.md)
  A structure for a set of muted processes.
- [func es_release_muted_processes(UnsafeMutablePointer<es_muted_processes_t>)](es_release_muted_processes(_:).md)
  Frees resources associated with a set of previously-retrieved muted processes.
- [func es_muted_processes_events(OpaquePointer, UnsafeMutablePointer<UnsafeMutablePointer<es_muted_processes_t>?>) -> es_return_t](es_muted_processes_events(_:_:).md)
  Retrieve a list of all muted processes.
- [func es_mute_path(OpaquePointer, UnsafePointer<CChar>, es_mute_path_type_t) -> es_return_t](es_mute_path(_:_:_:).md)
  Suppresses events from executables that match a given path.
- [func es_mute_path_events(OpaquePointer, UnsafePointer<CChar>, es_mute_path_type_t, UnsafePointer<es_event_type_t>, Int) -> es_return_t](es_mute_path_events(_:_:_:_:_:).md)
  Suppresses a subset of events from executables that match a given path.
- [struct es_mute_path_type_t](es_mute_path_type_t.md)
  The type of a path argument, such as a prefix or a path literal.
- [func es_muted_paths_events(OpaquePointer, UnsafeMutablePointer<UnsafeMutablePointer<es_muted_paths_t>>?) -> es_return_t](es_muted_paths_events(_:_:).md)
  Retrieve a list of all muted paths.
- [func es_release_muted_paths(UnsafeMutablePointer<es_muted_paths_t>)](es_release_muted_paths(_:).md)
  Frees resources associated with a set of previously-retrieved muted paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_muted_paths_t)*