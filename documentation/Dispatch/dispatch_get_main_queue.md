# dispatch_get_main_queue

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Returns the serial dispatch queue associated with the application’s main thread.

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
static dispatch_queue_main_tdispatch_get_main_queue();
```

#### Return Value

Returns the main queue. This queue is created automatically on behalf of the main thread before `main` is called.

#### Discussion

The system automatically creates the main queue and associates it with your application’s main thread. Your app uses one (and only one) of the following three approaches to invoke blocks submitted to the main queue:

- Calling [`dispatchMain()`](./dispatchmain%28%29.md)
- Calling [`UIApplicationMain(_:_:_:_:)`](../UIKit/uiapplicationmain%28_,_,_,_%29-1yub7.md) (iOS) or [`NSApplicationMain(_:_:)`](../AppKit/nsapplicationmain%28_,_%29.md) (macOS)
- Using a [`CFRunLoop`](../CoreFoundation/cfrunloop.md) on the main thread

As with the global concurrent queues, calls to [`suspend()`](./dispatchobject/suspend%28%29.md), [`resume()`](./dispatchobject/resume%28%29.md), [`dispatch_set_context`](./dispatch_set_context.md), and the like have no effect when used with queues returned by this function.

## See Also

### Related Documentation
- [Concurrency Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091)
### Queues and Tasks
- [dispatch_get_global_queue](./dispatch_get_global_queue.md)
  Returns a system-defined global concurrent queue with the specified quality-of-service class.
- [Dispatch Queue](./dispatch-queue.md)
  An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.
- [Dispatch Work Item](./dispatch-work-item.md)
  The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [Dispatch Group](./dispatch-group.md)
  A group of tasks that you monitor as a single unit.
- [Workloop](./workloop.md)
  A dispatch object that prioritizes the execution of tasks based on their quality-of-service (QoS) level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_get_main_queue)*