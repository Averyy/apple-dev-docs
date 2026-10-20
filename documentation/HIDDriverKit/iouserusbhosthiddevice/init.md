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

#### Return Value

`true` if initialization was successful, or `false` if an error occurred.

## See Also

### Running the Service
- [Start](./start.md)
  Starts the current device service and associates it with the specified provider object.
- [handleStart](./handlestart.md)
  Performs any custom initialization associated with starting the device service.
- [Stop](./stop.md)
  Stops the device service associated with the specified provider.
- [free](./free.md)
  Performs any final cleanup for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/init)*