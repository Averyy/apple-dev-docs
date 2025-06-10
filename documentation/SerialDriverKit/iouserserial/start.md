# Start

**Framework**: SerialDriverKit  
**Kind**: method

Starts the current service and associates it with the specified provider.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t Start(IOService * provider);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

After successfully matching the specified `provider` to your driver’s service, the system instantiates your service object and calls this method. Use this method to perform any additional configuration of your driver, and then call the [`RegisterService`](https://developer.apple.com/documentation/DriverKit/IOService/RegisterService) method to let the system know that your service is running. For example, you might use this method to store a reference to the specified provider object for later use. Always call `super` early in your implementation of this method.

You don’t need to open a communications channel to your device in this method. The system calls your service’s [`HwActivate`](iouserserial/hwactivate.md) method separately to activate your hardware.

## Parameters

- `provider`: The provider object that matches the current service. Cast this object to the class you expect. The system retains this object for the duration of your   method. The system continues to retain the object if your service starts successfully, releasing it only after calling your service’s   method.

## See Also

- [init](iouserserial/init.md)
  Handles the basic initialization of the service.
- [Stop](iouserserial/stop.md)
  Stops the service associated with the specified provider.
- [free](iouserserial/free.md)
  Performs any final cleanup for the service.
- [initWith](iouserserial/initwith.md)
  Initializes the private data structures associated with this class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial/start)*