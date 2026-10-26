# dispatch_queue_create_with_target

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Creates a new dispatch queue to which you can submit blocks.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```c
extern dispatch_queue_tdispatch_queue_create_with_target(const char *label, dispatch_queue_attr_t attr, dispatch_queue_t target);
```

#### Return Value

The newly created dispatch queue.

## Parameters

- `label`: A string label to attach to the queue to uniquely identify it in debugging tools such as Instruments, sample, stackshots, and crash reports.  Because applications, libraries, and frameworks can all create their own dispatch queues, a reverse-DNS naming style (*com.example.myqueue*) is recommended.  This parameter is optional and can be `NULL`.
- `attr`: The queue attributes. Specify [`DISPATCH_QUEUE_SERIAL`](./dispatch_queue_serial.md) (or `NULL`) to create a serial queue or specify [`DISPATCH_QUEUE_CONCURRENT`](./dispatch_queue_concurrent.md) to create a concurrent queue.
- `target`: The target queue on which to execute blocks. This method retains the target queue. Specify `DISPATCH_TARGET_QUEUE_DEFAULT` to set the target queue to the default type for the current dispatch queue.

## See Also

### Creating a Dispatch Queue
- [dispatch_get_main_queue](./dispatch_get_main_queue.md)
  Returns the serial dispatch queue associated with the application’s main thread.
- [dispatch_get_global_queue](./dispatch_get_global_queue.md)
  Returns a system-defined global concurrent queue with the specified quality-of-service class.
- [dispatch_queue_create](./dispatch_queue_create.md)
  Creates a new dispatch queue to which you can submit blocks.
- [DISPATCH_QUEUE_SERIAL](./dispatch_queue_serial.md)
  A dispatch queue that executes blocks serially in FIFO order.
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

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_queue_create_with_target)*