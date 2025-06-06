# handleStart

**Framework**: HIDDriverKit  
**Kind**: method

Performs additional initialization during the startup of the event service.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
bool handleStart(IOService * provider);
```

#### Return Value

`true` if initialization was successful, or `false` if an error occurred.

#### Discussion

The default implemention of this method does nothing.

## Parameters

- `provider`: The   provider for this object.

## See Also

- [init](iouserhideventservice/init.md)
  Handles the basic initialization of the event service.
- [Start](iouserhideventservice/start.md)
  Starts the current event service and associates it with the specified provider object.
- [Stop](iouserhideventservice/stop.md)
  Stops the event service associated with the specified provider.
- [free](iouserhideventservice/free.md)
  Performs any final cleanup for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventservice/handlestart)*