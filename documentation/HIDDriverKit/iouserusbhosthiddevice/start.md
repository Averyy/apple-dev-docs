# Start

**Framework**: HIDDriverKit  
**Kind**: method

Starts the current device service and associates it with the specified provider object.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
kern_return_t Start(IOService * provider);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

After successfully matching the specified provider to your device, the system instantiates your device object and calls this method. This method configures the USB device and sets up the pipes needed for communication.

Don’t override this method directly. Instead, implement your custom initialization code in the [`handleStart`](iouserhiddevice/handlestart.md) method.

## Parameters

- `provider`: The provider object that matches the current service. This method requires that the provider be an   object, and returns an error if it isn’t. The system retains this object for the duration of the   method. The system continues to retain the object if your service starts successfully, releasing it only after calling your service’s   method.

## See Also

- [init](iouserusbhosthiddevice/init.md)
  Handles the basic initialization of the event service.
- [handleStart](iouserusbhosthiddevice/handlestart.md)
  Performs any custom initialization associated with starting the device service.
- [Stop](iouserusbhosthiddevice/stop.md)
  Stops the device service associated with the specified provider.
- [free](iouserusbhosthiddevice/free.md)
  Performs any final cleanup for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/start)*