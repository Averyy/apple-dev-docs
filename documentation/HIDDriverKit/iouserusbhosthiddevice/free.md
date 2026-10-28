# free

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Performs any final cleanup for the service.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual void free();
```

## Discussion

Use this method to perform any final cleanup of your device service, such as deallocating memory you allocated. The system calls this method at some point after it calls your service’s [`Stop`](../iouserhideventservice/stop.md) method.

Always call `super` at the end of your custom implementation.

## See Also

### Running the Service
- [init](./init.md)
  Handles the basic initialization of the event service.
- [Start](./start.md)
  Starts the current device service and associates it with the specified provider object.
- [handleStart](./handlestart.md)
  Performs any custom initialization associated with starting the device service.
- [Stop](./stop.md)
  Stops the device service associated with the specified provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/free)*