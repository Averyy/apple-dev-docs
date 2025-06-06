# Start

**Framework**: AudioDriverKit  
**Kind**: method

Starts the current service and associates it with the specified provider.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t Start(IOService * provider);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Override this method inherited from [`IOService`](https://developer.apple.com/documentation/DriverKit/IOService).

After successfully matching the specified provider to your driver’s service, the system instantiates your service object and calls this method. Use this method to configure your driver’s data structures and setup the associated hardware. You might also store a reference to the `provider` object for later use. After you configure your driver, call the [`RegisterService`](https://developer.apple.com/documentation/kernel/ioservice/3180701-registerservice) method to let the system know your service is running.

Always call `super` early in your implementation of this method.

## Parameters

- `provider`: The provider object that matches the current service. Cast this object to the class you expect. The system retains this object for the duration of your   method. The system continues to retain the object if your service starts successfully, releasing it only after calling your service’s   method.

## See Also

- [init](iouseraudiodriver/init.md)
  Handles the basic initialization of the service.
- [Stop](iouseraudiodriver/stop.md)
  Stops the service associated with the specified provider.
- [free](iouseraudiodriver/free.md)
  Performs any final cleanup for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/start)*