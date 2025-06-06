# sync(execute:)

**Framework**: Dispatch  
**Kind**: method

Submits a block object for execution and returns after that block finishes executing.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func sync(execute block: () -> Void)
```

#### Discussion

This function submits a block to the specified dispatch queue for synchronous execution. Unlike [`dispatch_async`](dispatch_async.md), this function does not return until the block has finished. Calling this function and targeting the current queue results in deadlock.

Unlike with [`dispatch_async`](dispatch_async.md), no retain is performed on the target queue. Because calls to this function are synchronous, it “borrows” the reference of the caller. Moreover, no `Block_copy` is performed on the block.

As a performance optimization, this function executes blocks on the current thread whenever possible, with one exception: Blocks submitted to the main dispatch queue always run on the main thread.

## Parameters

- `block`: The block that contains the work to perform. This block has no return value and no parameters. This parameter cannot be  .

## See Also

- [func sync(execute: DispatchWorkItem)](dispatchqueue/sync(execute:)-2fzvo.md)
  Submits a work item for execution on the current queue and returns after that block finishes executing.
- [func sync<T>(execute: () throws -> T) rethrows -> T](dispatchqueue/sync(execute:)-20xby.md)
  Submits a work item for execution and returns the results from that item after it finishes executing.
- [func sync<T>(flags: DispatchWorkItemFlags, execute: () throws -> T) rethrows -> T](dispatchqueue/sync(flags:execute:).md)
  Submits a work item for execution using the specified attributes and returns the results from that item after it finishes executing.
- [func asyncAndWait(execute: () -> Void)](dispatchqueue/asyncandwait(execute:)-1udeu.md)
  Submits a work item for execution and returns only after it finishes executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/sync(execute:)-3segw)*