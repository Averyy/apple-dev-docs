# Cancel

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Cancel all callbacks from the dispatch source.

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

Subclasses must provide an implementation of this method. After cancellation, the dispatch source can only be freed. It cannot be reactivated.

## Parameters

- `handler`: The handler block to execute after the dispatch source finishes any in-flight callbacks.

## See Also

### Configuring the Dispatch Source
- [init](./init.md)
  Handles the basic initialization of the dispatch source.
- [free](./free.md)
  Performs any final cleanup for the dispatch source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchsource/cancel)*