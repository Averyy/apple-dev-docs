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

Use this method to perform any final cleanup of your event driver, such as deallocating memory you allocated. The system calls this method at some point after it calls your service’s [`Stop`](iouserhideventservice/stop.md) method.

Always call `super` at the end of your custom implementation.

## See Also

- [init](iouserhideventdriver/init.md)
  Handles the basic initialization of the event service.
- [Start](iouserhideventdriver/start.md)
  Starts the current event driver and associates it with the specified provider object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventdriver/free)*