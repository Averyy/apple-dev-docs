# DISPATCH_QUEUE_SERIAL

**Framework**: Dispatch  
**Kind**: macro  
**Role**: Macro

A dispatch queue that executes blocks serially in FIFO order.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
#define DISPATCH_QUEUE_SERIAL
```

## See Also

### Creating a Dispatch Queue
- [dispatch_get_main_queue](./dispatch_get_main_queue.md)
  Returns the serial dispatch queue associated with the application’s main thread.
- [dispatch_get_global_queue](./dispatch_get_global_queue.md)
  Returns a system-defined global concurrent queue with the specified quality-of-service class.
- [dispatch_queue_create](./dispatch_queue_create.md)
  Creates a new dispatch queue to which you can submit blocks.
- [dispatch_queue_create_with_target](./dispatch_queue_create_with_target.md)
  Creates a new dispatch queue to which you can submit blocks.
- [DISPATCH_QUEUE_CONCURRENT](./dispatch_queue_concurrent.md)
  A dispatch queue that executes blocks concurrently.
- [typealias dispatch_queue_t](./dispatch_queue_t.md)
  A lightweight object to which your application submits blocks for subsequent execution.
- [typealias dispatch_queue_main_t](./dispatch_queue_main_t.md)
  A dispatch queue that is bound to the app’s main thread and executes tasks serially on that thread.
- [typealias dispatch_queue_global_t](./dispatch_queue_global_t.md)
  A dispatch queue that executes tasks concurrently using threads from the global thread pool.
- [typealias dispatch_queue_serial_t](./dispatch_queue_serial_t.md)
  A dispatch queue that executes tasks serially in first-in, first-out (FIFO) order.
- [typealias dispatch_queue_concurrent_t](./dispatch_queue_concurrent_t.md)
  A dispatch queue that executes tasks concurrently and in any order, respecting any barriers that may be in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_queue_serial)*