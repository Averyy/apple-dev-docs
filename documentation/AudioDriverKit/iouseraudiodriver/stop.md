# Stop

**Framework**: AudioDriverKit  
**Kind**: method

Stops the service associated with the specified provider.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t Stop(IOService * provider);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Override this method inherited from [`IOService`](https://developer.apple.com/documentation/DriverKit/IOService).

Before terminating the object in `provider`, the system calls this method to stop the service associated with that object. Use your implementation of this method to stop all activity and put your driver in a quiescent state. If your driver has any in-progress asynchronous tasks, cancel those tasks and wait for DriverKit to call the associated cancellation handler before calling the super version of this method.

Call super at the end of your implementation. After you call `super`, it is a programmer error to access the provider object.

Don’t use this method to release your `ivars` structure; use the [`free`](iouseraudiodriver/free.md) method instead.

## Parameters

- `provider`: The provider associated with the current service. This object is the same one that the system previously passed to your service’s   method.

## See Also

- [init](iouseraudiodriver/init.md)
  Handles the basic initialization of the service.
- [Start](iouseraudiodriver/start.md)
  Starts the current service and associates it with the specified provider.
- [free](iouseraudiodriver/free.md)
  Performs any final cleanup for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/stop)*