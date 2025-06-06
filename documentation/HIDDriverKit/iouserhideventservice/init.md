# init

**Framework**: HIDDriverKit  
**Kind**: method

Handles the basic initialization of the event service.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
bool init();
```

#### Return Value

`true` if initialization was successful, or `false` if an error occurred.

## See Also

- [Start](iouserhideventservice/start.md)
  Starts the current event service and associates it with the specified provider object.
- [handleStart](iouserhideventservice/handlestart.md)
  Performs additional initialization during the startup of the event service.
- [Stop](iouserhideventservice/stop.md)
  Stops the event service associated with the specified provider.
- [free](iouserhideventservice/free.md)
  Performs any final cleanup for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventservice/init)*