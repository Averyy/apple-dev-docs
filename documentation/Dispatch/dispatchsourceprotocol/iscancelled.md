# isCancelled

**Framework**: Dispatch  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean indicating whether the given dispatch source has been canceled.

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
var isCancelled: Bool { get }
```

## See Also

### Canceling a Dispatch Source
- [func cancel()](./cancel%28%29.md)
  Asynchronously cancels the dispatch source, preventing any further invocation of its event handler block.
- [func setCancelHandler(handler: DispatchWorkItem)](./setcancelhandler%28handler%29.md)
  Sets the cancellation handler block for the dispatch source.
- [func setCancelHandler(qos: DispatchQoS, flags: DispatchWorkItemFlags, handler: Self.DispatchSourceHandler?)](./setcancelhandler%28qos,flags,handler%29.md)
  Sets the cancellation handler block for the dispatch source with the specified quality-of-service class and work item options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol/iscancelled)*