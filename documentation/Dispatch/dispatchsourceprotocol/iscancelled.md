# isCancelled

**Framework**: Dispatch  
**Kind**: property

Returns a Boolean indicating whether the given dispatch source has been canceled.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var isCancelled: Bool { get }
```

## See Also

- [func cancel()](dispatchsourceprotocol/cancel.md)
  Asynchronously cancels the dispatch source, preventing any further invocation of its event handler block.
- [func setCancelHandler(handler: DispatchWorkItem)](dispatchsourceprotocol/setcancelhandler(handler:).md)
  Sets the cancellation handler block for the dispatch source.
- [func setCancelHandler(qos: DispatchQoS, flags: DispatchWorkItemFlags, handler: Self.DispatchSourceHandler?)](dispatchsourceprotocol/setcancelhandler(qos:flags:handler:).md)
  Sets the cancellation handler block for the dispatch source with the specified quality-of-service class and work item options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol/iscancelled)*