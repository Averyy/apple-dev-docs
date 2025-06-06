# es_thread_t

**Framework**: Endpoint Security  
**Kind**: struct

A structure that represents a thread in a process.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_thread_t
```

## Topics

### Identifying the Thread
- [var thread_id: UInt64](es_thread_t/thread_id.md)
  The unique identifier of the thread.
### Initializers
- [init()](es_thread_t/init.md)
- [init(thread_id: UInt64)](es_thread_t/init(thread_id:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var thread: UnsafeMutablePointer<es_thread_t>?](es_message_t/thread.md)
  The thread that took the action defined in a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_thread_t)*