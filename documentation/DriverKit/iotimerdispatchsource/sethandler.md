# SetHandler

**Framework**: DriverKit  
**Kind**: method

Sets the handler block to run when the timer fires.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t SetHandler(OSAction * action);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. See [`Error Codes`](error-codes.md).

## Parameters

- `action`: The   object that contains your custom callback method. The dispatch source object retains your action object until you call this method again or cancel the dispatch source.

## See Also

- [Create](iotimerdispatchsource/create.md)
  Creates and configures a timer dispatch object.
- [init](iotimerdispatchsource/init.md)
  Handles the basic initialization of the dispatch source.
- [free](iotimerdispatchsource/free.md)
  Performs any final cleanup for the timer dispatch source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iotimerdispatchsource/sethandler)*