# es_unmute_process(_:_:)

**Framework**: Endpoint Security  
**Kind**: func

Restores event delivery from a previously-muted process.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func es_unmute_process(_ client: OpaquePointer, _ audit_token: UnsafePointer<audit_token_t>) -> es_return_t
```

#### Return Value

A value that indicates whether the unmute request succeeded or failed with an error.

#### Discussion

To unmute a subset of events from a process, use [`es_unmute_process_events(_:_:_:_:)`](es_unmute_process_events(_:_:_:_:).md).

## Parameters

- `client`: A previously-muted client. If the call succeeds, this client begins to receive events from the process indicated by  .
- `audit_token`: The audit token indicating the process to unmute.

## See Also

- [func es_unmute_process_events(OpaquePointer, UnsafePointer<audit_token_t>, UnsafePointer<es_event_type_t>, Int) -> es_return_t](es_unmute_process_events(_:_:_:_:).md)
  Restores event delivery of a subset of events from a previously-muted process.
- [func es_unmute_path(OpaquePointer, UnsafePointer<CChar>, es_mute_path_type_t) -> es_return_t](es_unmute_path(_:_:_:).md)
  Restores event delivery from a previously-muted path.
- [func es_unmute_path_events(OpaquePointer, UnsafePointer<CChar>, es_mute_path_type_t, UnsafePointer<es_event_type_t>, Int) -> es_return_t](es_unmute_path_events(_:_:_:_:_:).md)
  Restores event delivery of a subset of events from a previously-muted path.
- [struct es_mute_path_type_t](es_mute_path_type_t.md)
  The type of a path argument, such as a prefix or a path literal.
- [func es_unmute_all_paths(OpaquePointer) -> es_return_t](es_unmute_all_paths(_:).md)
  Restores event delivery from previously-muted paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_unmute_process(_:_:))*