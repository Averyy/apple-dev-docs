# Cancel

**Framework**: DriverKit  
**Kind**: method

Cancels all callbacks from the dispatch source.

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

After cancelling a dispatch source, you cannot reactivate it.

## Parameters

- `handler`: The handler block to call after any in-flight callbacks finish executing.

## See Also

- [SetEnableWithCompletion](iodataqueuedispatchsource/setenablewithcompletion.md)
  Controls the enable state of the interrupt source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/cancel)*