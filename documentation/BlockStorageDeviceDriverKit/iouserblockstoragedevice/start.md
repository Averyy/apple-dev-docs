# Start

**Framework**: BlockStorageDeviceDriverKit  
**Kind**: method

Starts the current service and associates it with the specified provider.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t Start(IOService * provider);
```

#### Return Value

A value that indicates the service-starting result. Return [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) to inidicate success. To indicate a failure, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants) for error definitions.

#### Discussion

After successfully matching the specified `provider` to your driver’s service, the system instantiates your service object and calls this method. Use this method to configure your driver’s data structures and setup the associated hardware. You might also store a reference to the `provider` object for later use. After configuring your driver, call the [`RegisterService`](https://developer.apple.com/documentation/DriverKit/IOService/RegisterService) method to let the system know your service is running.

Always call `super` early in your implementation of this method.

## Parameters

- `provider`: The provider object that matches the current service. Cast this object to the class you expect. The system retains this object for the duration of your   method. The system continues to retain the object if your service starts successfully, releasing it only after calling your service’s   method.

## See Also

- [init](iouserblockstoragedevice/init.md)
  Handles the basic initialization of the service.
- [Stop](iouserblockstoragedevice/stop.md)
  Stops the service associated with the specified provider.
- [free](iouserblockstoragedevice/free.md)
  Performs any final cleanup for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/blockstoragedevicedriverkit/iouserblockstoragedevice/start)*