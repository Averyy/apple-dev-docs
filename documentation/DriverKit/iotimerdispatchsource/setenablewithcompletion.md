# SetEnableWithCompletion

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Enables or disables the timer.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual kern_return_t SetEnableWithCompletion(bool enable, IODispatchSourceCancelHandler handler);
```

## Return Value

[`kIOReturnSuccess`](../kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../error-codes.md).

## Parameters

- `enable`: A Boolean value that indicates whether to enable or disable the timer. Specify [`true`](../../Swift/true.md) to enable the timer or [`false`](../../Swift/false.md) to disable it.
- `handler`: An optional block to execute after any pending handlers of a newly disabled timer finish executing.

## See Also

### Starting and Stopping the Timer Source
- [Cancel](./cancel.md)
  Cancels all callbacks from the event source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iotimerdispatchsource/setenablewithcompletion)*