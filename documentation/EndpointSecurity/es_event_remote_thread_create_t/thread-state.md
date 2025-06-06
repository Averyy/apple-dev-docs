# thread_state

**Framework**: Endpoint Security  
**Kind**: property

The new thread’s state.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var thread_state: UnsafeMutablePointer<es_thread_state_t>?
```

#### Discussion

When creating a thread with `thread_create_running(_:_:_:_:_:)`, this value contains an [`es_thread_state_t`](es_thread_state_t.md) value. When using `thread_create(_:_:)`, this value is `NULL`.

## See Also

- [var target: UnsafeMutablePointer<es_process_t>](es_event_remote_thread_create_t/target.md)
  The process targeted to spawn a new thread.
- [struct es_thread_state_t](es_thread_state_t.md)
  A description of a thread’s machine-specfiic state.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_remote_thread_create_t/reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_remote_thread_create_t/thread_state)*