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

#### Return Value

`true` if initialization was successful, or `false` if an error occurred.

#### Discussion

Don’t call this method directly. Call [`Create`](./create.md) when you want to create a new data-queue dispatch source.

## See Also

### Configuring the Dispatch Source
- [Create](./create.md)
  Creates a dispatch source that you use as a shared-memory data queue.
- [free](./free.md)
  Performs any final cleanup for the data-queue dispatch source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/init)*