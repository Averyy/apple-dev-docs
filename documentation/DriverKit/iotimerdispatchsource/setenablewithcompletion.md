# SetEnableWithCompletion

**Framework**: DriverKit  
**Kind**: method

Enables or disables the timer.

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

- `enable`: A Boolean value that indicates whether to enable or disable the timer. Specify   to enable the timer or   to disable it.
- `handler`: An optional block to execute after any pending handlers of a newly disabled timer finish executing.

## See Also

- [Cancel](iotimerdispatchsource/cancel.md)
  Cancels all callbacks from the event source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iotimerdispatchsource/setenablewithcompletion)*