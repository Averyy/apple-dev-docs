# cancel()

**Framework**: Dispatch  
**Kind**: method  
**Role**: Instance Method

Asynchronously cancels the dispatch source, preventing any further invocation of its event handler block.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func cancel()
```

#### Discussion

Cancellation prevents any further invocation of the event handler block for the dispatch source, but does not interrupt any work that is already in progress. If a cancellation handler was set before cancellation, it is sub mitted to the target queue once any in-progress event handler work is finished. Once the cancellation handler is submitted, it is safe to close the source’s handle (file descriptor or mach port). It is invalid to close a file descriptor or deallocate a mach port that is currently being tracked by a dispatch source object before the cancellation handler is invoked.

## See Also

### Canceling a Dispatch Source
- [var isCancelled: Bool](./iscancelled.md)
  Returns a Boolean indicating whether the given dispatch source has been canceled.
- [func setCancelHandler(handler: DispatchWorkItem)](./setcancelhandler%28handler%29.md)
  Sets the cancellation handler block for the dispatch source.
- [func setCancelHandler(qos: DispatchQoS, flags: DispatchWorkItemFlags, handler: Self.DispatchSourceHandler?)](./setcancelhandler%28qos,flags,handler%29.md)
  Sets the cancellation handler block for the dispatch source with the specified quality-of-service class and work item options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol/cancel())*