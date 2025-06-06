# SetEnableWithCompletion

**Framework**: DriverKit  
**Kind**: method

Controls the enable state of the interrupt source.

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

- `enable`: A Boolean value that indicates whether to enable the dispatch source. Specify   to enable the source or   to disable it.
- `handler`: An optional block to execute after this method successfully disables the dispatch source.

## See Also

- [Cancel](iodataqueuedispatchsource/cancel.md)
  Cancels all callbacks from the dispatch source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/setenablewithcompletion)*