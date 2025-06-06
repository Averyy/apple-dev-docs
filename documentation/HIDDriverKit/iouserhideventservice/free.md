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

Use this method to perform any final cleanup of your event service, such as deallocating memory you allocated. The system calls this method at some point after it calls your service’s [`Stop`](iouserhideventservice/stop.md) method.

Always call `super` at the end of your custom implementation.

## See Also

- [init](iouserhideventservice/init.md)
  Handles the basic initialization of the event service.
- [Start](iouserhideventservice/start.md)
  Starts the current event service and associates it with the specified provider object.
- [handleStart](iouserhideventservice/handlestart.md)
  Performs additional initialization during the startup of the event service.
- [Stop](iouserhideventservice/stop.md)
  Stops the event service associated with the specified provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventservice/free)*