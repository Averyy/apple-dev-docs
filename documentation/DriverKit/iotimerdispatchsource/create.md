# Create

**Framework**: DriverKit  
**Kind**: method

Creates and configures a timer dispatch object.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static kern_return_t Create(IODispatchQueue * queue, IOTimerDispatchSource * * source);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. See [`Error Codes`](error-codes.md).

## Parameters

- `queue`: The dispatch queue on which to run any handler blocks.
- `source`: A variable for storing the dispatch source. On return, this variable contains the retained object. You are responsible for releasing this object.

## See Also

- [init](iotimerdispatchsource/init.md)
  Handles the basic initialization of the dispatch source.
- [free](iotimerdispatchsource/free.md)
  Performs any final cleanup for the timer dispatch source.
- [SetHandler](iotimerdispatchsource/sethandler.md)
  Sets the handler block to run when the timer fires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iotimerdispatchsource/create)*