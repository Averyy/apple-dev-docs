# es_unmute_all_paths(_:)

**Framework**: Endpoint Security  
**Kind**: func

Restores event delivery from previously-muted paths.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func es_unmute_all_paths(_ client: OpaquePointer) -> es_return_t
```

## Parameters

- `client`: The client for which to unmute events.

## See Also

- [func es_unmute_process(OpaquePointer, UnsafePointer<audit_token_t>) -> es_return_t](es_unmute_process(_:_:).md)
  Restores event delivery from a previously-muted process.
- [func es_unmute_process_events(OpaquePointer, UnsafePointer<audit_token_t>, UnsafePointer<es_event_type_t>, Int) -> es_return_t](es_unmute_process_events(_:_:_:_:).md)
  Restores event delivery of a subset of events from a previously-muted process.
- [func es_unmute_path(OpaquePointer, UnsafePointer<CChar>, es_mute_path_type_t) -> es_return_t](es_unmute_path(_:_:_:).md)
  Restores event delivery from a previously-muted path.
- [func es_unmute_path_events(OpaquePointer, UnsafePointer<CChar>, es_mute_path_type_t, UnsafePointer<es_event_type_t>, Int) -> es_return_t](es_unmute_path_events(_:_:_:_:_:).md)
  Restores event delivery of a subset of events from a previously-muted path.
- [struct es_mute_path_type_t](es_mute_path_type_t.md)
  The type of a path argument, such as a prefix or a path literal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_unmute_all_paths(_:))*