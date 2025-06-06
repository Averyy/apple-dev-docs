# free

**Framework**: HIDDriverKit  
**Kind**: method

Performs any final cleanup for the service.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
void free();
```

#### Discussion

Use this method to perform any final cleanup of your device service, such as deallocating memory you allocated. The system calls this method at some point after it calls your service’s [`Stop`](iouserhideventservice/stop.md) method.

Always call `super` at the end of your custom implementation.

## See Also

- [init](iouserusbhosthiddevice/init.md)
  Handles the basic initialization of the event service.
- [Start](iouserusbhosthiddevice/start.md)
  Starts the current device service and associates it with the specified provider object.
- [handleStart](iouserusbhosthiddevice/handlestart.md)
  Performs any custom initialization associated with starting the device service.
- [Stop](iouserusbhosthiddevice/stop.md)
  Stops the device service associated with the specified provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/free)*