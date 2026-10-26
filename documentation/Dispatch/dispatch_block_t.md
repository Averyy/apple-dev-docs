# dispatch_block_t

**Framework**: Dispatch  
**Kind**: typealias  
**Role**: Type Alias

The prototype of blocks submitted to dispatch queues, which take no arguments and have no return value.

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
typedef void (^)(void) dispatch_block_t;
```

#### Discussion

Blocks behave like other Objective-C objects. Under ARC, the system releases and retains them automatically, and it converts them to malloc blocks as needed to facilitate their escape from the current scope of execution. When ARC is disabled, you are responsible for retaining and releasing blocks at appropriate times, and for copying blocks before allowing them to escape from the current scope of execution.

## See Also

### Executing Tasks Asynchronously
- [dispatch_async](./dispatch_async.md)
  Submits a block for asynchronous execution on a dispatch queue and returns immediately.
- [dispatch_async_f](./dispatch_async_f.md)
  Submits an app-defined function for asynchronous execution on a dispatch queue and returns immediately.
- [dispatch_after](./dispatch_after.md)
  Enqueues a block for execution at the specified time.
- [dispatch_after_f](./dispatch_after_f.md)
  Enqueues an app-defined function for execution at the specified time.
- [dispatch_function_t](./dispatch_function_t.md)
  The prototype of functions submitted to dispatch queues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_block_t)*