# dispatch_queue_create

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Creates a new dispatch queue to which you can submit blocks.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern dispatch_queue_tdispatch_queue_create(const char *label, dispatch_queue_attr_t attr);
```

## Return Value

The newly created dispatch queue.

## Discussion

Blocks submitted to a serial queue are executed one at a time in FIFO order. Note, however, that blocks submitted to independent queues may be executed concurrently with respect to each other. Blocks submitted to a concurrent queue are dequeued in FIFO order but may run concurrently if resources are available to do so.

If your app isn’t using ARC, you should call [`dispatch_release`](./dispatch_release.md) on a dispatch queue when it’s no longer needed. Any pending blocks submitted to a queue hold a reference to that queue, so the queue is not deallocated until all pending blocks have completed.

## Parameters

- `label`: A string label to attach to the queue to uniquely identify it in debugging tools such as Instruments, `sample`, stackshots, and crash reports.  Because applications, libraries, and frameworks can all create their own dispatch queues, a reverse-DNS naming style (*com.example.myqueue*) is recommended.  This parameter is optional and can be `NULL`.
- `attr`: In macOS 10.7 and later or iOS 4.3 and later, specify [`DISPATCH_QUEUE_SERIAL`](./dispatch_queue_serial.md) (or `NULL`) to create a serial queue or specify [`DISPATCH_QUEUE_CONCURRENT`](./dispatch_queue_concurrent.md) to create a concurrent queue. In earlier versions, you must specify `NULL` for this parameter.

## See Also

### Creating a Dispatch Queue
- [dispatch_get_main_queue](./dispatch_get_main_queue.md)
  Returns the serial dispatch queue associated with the application’s main thread.
- [dispatch_get_global_queue](./dispatch_get_global_queue.md)
  Returns a system-defined global concurrent queue with the specified quality-of-service class.
- [dispatch_queue_create_with_target](./dispatch_queue_create_with_target.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_queue_create)*