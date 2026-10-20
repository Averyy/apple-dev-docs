# Cancel

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Cancels all callbacks from the event source.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual kern_return_t Cancel(IODispatchSourceCancelHandler handler);
```

#### Return Value

[`kIOReturnSuccess`](../kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../error-codes.md).

#### Discussion

After cancellation, the source can only be freed. It cannot be reactivated.

## Parameters

- `handler`: The handler block to execute after any interrupt callbacks finish.

## See Also

### Starting and Stopping the Interrupt Source
- [SetEnableWithCompletion](./setenablewithcompletion.md)
  Enables or disables the delivery of interrupts.
- [IODispatchSourceCancelHandler](../iodispatchsourcecancelhandler.md)
  A block to execute when a canceled dispatch source stops executing tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iointerruptdispatchsource/cancel)*