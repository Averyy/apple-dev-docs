# Cancel

**Framework**: DriverKit  
**Kind**: method

Cancels all callbacks from the event source.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t Cancel(IODispatchSourceCancelHandlerhandler);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. See [`Error Codes`](error-codes.md).

#### Discussion

After cancellation, the source can only be freed. It cannot be reactivated.

## Parameters

- `handler`: The handler block to execute after the dispatch source finishes any in-flight callbacks.

## See Also

- [SetEnableWithCompletion](iotimerdispatchsource/setenablewithcompletion.md)
  Enables or disables the timer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iotimerdispatchsource/cancel)*