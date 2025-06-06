# setCancelHandler(qos:flags:handler:)

**Framework**: Dispatch  
**Kind**: method

Sets the cancellation handler block for the dispatch source with the specified quality-of-service class and work item options.

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
func setCancelHandler(qos: DispatchQoS = .unspecified, flags: DispatchWorkItemFlags = [], handler: Self.DispatchSourceHandler?)
```

#### Discussion

The cancellation handler (if specified) is submitted to the source’s target queue in response to a call to a call to the [`cancel()`](dispatchsourceprotocol/cancel().md) method once the system has released all references to the source’s underlying handle and the source’s event handler block has returned.

To safely close a file descriptor or destroy a Mach port, a cancellation handler is required for that descriptor or port. Closing the descriptor or port before the cancellation handler runs can result in a race condition. If a new descriptor is allocated with the same value as the recently closed descriptor while the source’s event handler is still running, the event handler may read/write data using the wrong descriptor.

## Parameters

- `qos`: The quality-of-service to apply to the handler block.
- `flags`: Configuration flags for the work item. For a list of possible values, see  .
- `handler`: The event handler block to submit to the source’s target queue.

## See Also

- [func cancel()](dispatchsourceprotocol/cancel.md)
  Asynchronously cancels the dispatch source, preventing any further invocation of its event handler block.
- [var isCancelled: Bool](dispatchsourceprotocol/iscancelled.md)
  Returns a Boolean indicating whether the given dispatch source has been canceled.
- [func setCancelHandler(handler: DispatchWorkItem)](dispatchsourceprotocol/setcancelhandler(handler:).md)
  Sets the cancellation handler block for the dispatch source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol/setcancelhandler(qos:flags:handler:))*