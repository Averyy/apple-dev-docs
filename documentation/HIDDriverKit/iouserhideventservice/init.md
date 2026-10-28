# init

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Handles the basic initialization of the event service.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual bool init();
```

## Return Value

`true` if initialization was successful, or `false` if an error occurred.

## See Also

### Running the Service
- [Start](./start.md)
  Starts the current event service and associates it with the specified provider object.
- [handleStart](./handlestart.md)
  Performs additional initialization during the startup of the event service.
- [Stop](./stop.md)
  Stops the event service associated with the specified provider.
- [free](./free.md)
  Performs any final cleanup for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventservice/init)*