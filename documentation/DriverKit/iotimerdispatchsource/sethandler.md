# SetHandler

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the handler block to run when the timer fires.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual kern_return_t SetHandler(OSAction *action);
```

#### Return Value

[`kIOReturnSuccess`](../kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../error-codes.md).

## Parameters

- `action`: The [`OSAction`](../osaction.md) object that contains your custom callback method. The dispatch source object retains your action object until you call this method again or cancel the dispatch source.

## See Also

### Configuring the Timer Source
- [Create](./create.md)
  Creates and configures a timer dispatch object.
- [init](./init.md)
  Handles the basic initialization of the dispatch source.
- [free](./free.md)
  Performs any final cleanup for the timer dispatch source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iotimerdispatchsource/sethandler)*