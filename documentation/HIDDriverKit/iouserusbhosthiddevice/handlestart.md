# handleStart

**Framework**: HIDDriverKit  
**Kind**: method

Performs any custom initialization associated with starting the device service.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
bool handleStart(IOService * provider);
```

#### Return Value

`true` if initialization was successful, or `false` if it wasn’t.

#### Discussion

When defining a custom service, override this method and use it to perform any custom initialization. For example, you might allocate memory for your service’s instance variables and store a reference to the provider object for later use. Always call the `super` implementation of this method at some point.

Don’t call this method yourself. The [`Start`](iouserhiddevice/start.md) method calls it when starting up the service.

## Parameters

- `provider`: The   provider for this object.

## See Also

- [init](iouserusbhosthiddevice/init.md)
  Handles the basic initialization of the event service.
- [Start](iouserusbhosthiddevice/start.md)
  Starts the current device service and associates it with the specified provider object.
- [Stop](iouserusbhosthiddevice/stop.md)
  Stops the device service associated with the specified provider.
- [free](iouserusbhosthiddevice/free.md)
  Performs any final cleanup for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/handlestart)*