# Cancel

**Framework**: DriverKit  
**Kind**: method

Cancel all callbacks from the dispatch source.

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

Subclasses must provide an implementation of this method. After cancellation, the dispatch source can only be freed. It cannot be reactivated.

## Parameters

- `handler`: The handler block to execute after the dispatch source finishes any in-flight callbacks.

## See Also

- [init](iodispatchsource/init.md)
  Handles the basic initialization of the dispatch source.
- [free](iodispatchsource/free.md)
  Performs any final cleanup for the dispatch source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchsource/cancel)*