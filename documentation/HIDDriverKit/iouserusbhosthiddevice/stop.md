# Stop

**Framework**: HIDDriverKit  
**Kind**: method

Stops the device service associated with the specified provider.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
kern_return_t Stop(IOService * provider);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Before terminating the object in `provider`, the system calls this method to stop the service associated with that object. Use your implementation of this method to stop all activity and put your driver in a quiescent state. Call `super` at the end of your implementation. After you call `super`, it is a programmer error to access the `provider` object.

## Parameters

- `provider`: The provider associated with the current service. This object is the same one that the system previously passed to your service’s   method.

## See Also

- [init](iouserusbhosthiddevice/init.md)
  Handles the basic initialization of the event service.
- [Start](iouserusbhosthiddevice/start.md)
  Starts the current device service and associates it with the specified provider object.
- [handleStart](iouserusbhosthiddevice/handlestart.md)
  Performs any custom initialization associated with starting the device service.
- [free](iouserusbhosthiddevice/free.md)
  Performs any final cleanup for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/stop)*