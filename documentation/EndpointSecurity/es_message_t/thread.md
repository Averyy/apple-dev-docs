# thread

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The thread that took the action defined in a message.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var thread: UnsafeMutablePointer<es_thread_t>?
```

```c
es_thread_t * thread;
```

#### Discussion

This field may be NULL when threading doesn’t apply. This includes trace events that describe calls to `ptrace(PT_TRACE_ME`) or code-signing invalidation events resulting from another process calling `csops(CS_OPS_MARKINVALID)`.

## See Also

### Inspecting Thread Properties
- [struct es_thread_t](../es_thread_t.md)
  A structure that represents a thread in a process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_message_t/thread)*