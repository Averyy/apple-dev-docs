# es_thread_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

A structure that represents a thread in a process.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_thread_t
```

```c
typedef struct { ... } es_thread_t;
```

## Topics

### Identifying the Thread
- [var thread_id: UInt64](./es_thread_t/thread_id.md)
  The unique identifier of the thread.
### Initializers
- [init()](./es_thread_t/init%28%29.md)
- [init(thread_id: UInt64)](./es_thread_t/init%28thread_id%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Inspecting Thread Properties
- [var thread: UnsafeMutablePointer<es_thread_t>?](./es_message_t/thread.md)
  The thread that took the action defined in a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_thread_t)*