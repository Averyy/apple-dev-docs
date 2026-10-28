# init

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Handles the basic initialization of the dispatch source.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual bool init();
```

## Return Value

[`true`](../../Swift/true.md) if initialization was successful, or [`false`](../../Swift/false.md) if an error occurred.

## Discussion

Don’t call this method directly. Call [`Create`](./create.md) when you want to create a new timer dispatch queue.

## See Also

### Configuring the Timer Source
- [Create](./create.md)
  Creates and configures a timer dispatch object.
- [free](./free.md)
  Performs any final cleanup for the timer dispatch source.
- [SetHandler](./sethandler.md)
  Sets the handler block to run when the timer fires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iotimerdispatchsource/init)*