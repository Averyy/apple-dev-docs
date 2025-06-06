# SetEnableWithCompletion

**Framework**: DriverKit  
**Kind**: method

Enables or disables the delivery of interrupts.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t SetEnableWithCompletion(bool enable, IODispatchSourceCancelHandlerhandler);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. See [`Error Codes`](error-codes.md).

## Parameters

- `enable`: A Boolean value that indicates whether to enable the dispatch source. Specify   to enable the dispatch source, or   to disable it.
- `handler`: An optional block to execute when disabling the dispatch source. The dispatch source executes it after all pending interrupts finish executing.

## See Also

- [Cancel](iointerruptdispatchsource/cancel.md)
  Cancels all callbacks from the event source.
- [IODispatchSourceCancelHandler](iodispatchsourcecancelhandler.md)
  A block to execute when a canceled dispatch source stops executing tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iointerruptdispatchsource/setenablewithcompletion)*