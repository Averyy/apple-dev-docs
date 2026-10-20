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

## See Also

### Configuring the Dispatch Source
- [free](./free.md)
  Performs any final cleanup for the dispatch source.
- [Cancel](./cancel.md)
  Cancel all callbacks from the dispatch source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchsource/init)*