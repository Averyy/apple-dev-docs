# init

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Initializes the dispatch queue object.

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

`true` if initialization was successful, or `false` if it was unsuccessful.

## Discussion

Do not call this method directly. Call [`Create`](./create.md) when you want to create a new dispatch queue.

## See Also

### Creating a Dispatch Queue
- [Create](./create.md)
  Creates a new dispatch queue object.
- [free](./free.md)
  Performs any final cleanup for the dispatch queue object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchqueue/init)*