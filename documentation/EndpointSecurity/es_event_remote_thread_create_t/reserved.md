# reserved

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

An unused field reserved for future use.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)
```

```c
uint8_t reserved[64];
```

## See Also

### Inspecting Event Properties
- [var target: UnsafeMutablePointer<es_process_t>](./target.md)
  The process targeted to spawn a new thread.
- [var thread_state: UnsafeMutablePointer<es_thread_state_t>?](./thread_state.md)
  The new thread’s state.
- [struct es_thread_state_t](../es_thread_state_t.md)
  A description of a thread’s machine-specfiic state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_remote_thread_create_t/reserved)*