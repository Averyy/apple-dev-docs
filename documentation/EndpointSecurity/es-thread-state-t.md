# es_thread_state_t

**Framework**: Endpoint Security  
**Kind**: struct

A description of a thread’s machine-specfiic state.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_thread_state_t
```

#### Overview

To work with thread state, see the definitions in the include file `mach/thread_status.h` and corresponding machine-dependent headers.

## Topics

### Inspecting Thread State
- [var flavor: Int32](es_thread_state_t/flavor.md)
  An indication of the representation of the machine-specific thread state.
- [var state: es_token_t](es_thread_state_t/state.md)
  The machine-specific thread state.
- [struct es_token_t](es_token_t.md)
  An arbitrary buffer of data with its size.
### Initializers
- [init()](es_thread_state_t/init.md)
- [init(flavor: Int32, state: es_token_t)](es_thread_state_t/init(flavor:state:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [var target: UnsafeMutablePointer<es_process_t>](es_event_remote_thread_create_t/target.md)
  The process targeted to spawn a new thread.
- [var thread_state: UnsafeMutablePointer<es_thread_state_t>?](es_event_remote_thread_create_t/thread_state.md)
  The new thread’s state.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](es_event_remote_thread_create_t/reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_thread_state_t)*