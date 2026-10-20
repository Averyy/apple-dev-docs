# es_mute_path_type_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

The type of a path argument, such as a prefix or a path literal.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_mute_path_type_t
```

```c
typedef enum { ... } es_mute_path_type_t;
```

## Topics

### Path Types
- [var ES_MUTE_PATH_TYPE_PREFIX: es_mute_path_type_t](./es_mute_path_type_prefix.md)
  A type for a path string used as a prefix.
- [var ES_MUTE_PATH_TYPE_LITERAL: es_mute_path_type_t](./es_mute_path_type_literal.md)
  A type for a path string used as a path literal.
### Initializers
- [init(UInt32)](./es_mute_path_type_t/init%28_%29.md)
- [init(rawValue: UInt32)](./es_mute_path_type_t/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./es_mute_path_type_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

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
- [func es_mute_path(OpaquePointer, UnsafePointer<CChar>, es_mute_path_type_t) -> es_return_t](./es_mute_path%28_,_,_%29.md)
  Suppresses events from executables that match a given path.
- [func es_mute_path_events(OpaquePointer, UnsafePointer<CChar>, es_mute_path_type_t, UnsafePointer<es_event_type_t>, Int) -> es_return_t](./es_mute_path_events%28_,_,_,_,_%29.md)
  Suppresses a subset of events from executables that match a given path.
- [func es_muted_paths_events(OpaquePointer, UnsafeMutablePointer<UnsafeMutablePointer<es_muted_paths_t>>?) -> es_return_t](./es_muted_paths_events%28_,_%29.md)
  Retrieve a list of all muted paths.
- [struct es_muted_paths_t](./es_muted_paths_t.md)
  A structure for a set of muted paths.
- [func es_release_muted_paths(UnsafeMutablePointer<es_muted_paths_t>)](./es_release_muted_paths%28_%29.md)
  Frees resources associated with a set of previously-retrieved muted paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_mute_path_type_t)*