# Start

**Framework**: HIDDriverKit  
**Kind**: method

Starts the current event service and associates it with the specified provider object.

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

After successfully matching the specified provider to your event service, the system instantiates your service object and calls this method. Use this method to configure your custom data structures and associated hardware. You might also store a reference to the provider object for later use. After you configure your event service, call the [`RegisterService`](https://developer.apple.com/documentation/DriverKit/IOService/RegisterService) method to let the system know that your service is running. If you encounter an error, return an appropriate error code without calling `RegisterService`.

Always call `super` early in your implementation of this method.

## Parameters

- `provider`: The provider object that matches the current service. Cast this object to the class you expect. The system retains this object for the duration of your   method. The system continues to retain the object if your service starts successfully, releasing it only after calling your service’s   method.

## See Also

- [init](iouserhideventservice/init.md)
  Handles the basic initialization of the event service.
- [handleStart](iouserhideventservice/handlestart.md)
  Performs additional initialization during the startup of the event service.
- [Stop](iouserhideventservice/stop.md)
  Stops the event service associated with the specified provider.
- [free](iouserhideventservice/free.md)
  Performs any final cleanup for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventservice/start)*