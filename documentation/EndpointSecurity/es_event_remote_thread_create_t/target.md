# target

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The process targeted to spawn a new thread.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var target: UnsafeMutablePointer<es_process_t>
```

```c
es_process_t * target;
```

## See Also

### Inspecting Event Properties
- [var thread_state: UnsafeMutablePointer<es_thread_state_t>?](./thread_state.md)
  The new thread’s state.
- [struct es_thread_state_t](../es_thread_state_t.md)
  A description of a thread’s machine-specfiic state.
- [var reserved: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_remote_thread_create_t/target)*