# Stop

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Stops the service associated with the specified provider.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual kern_return_t Stop(IOService *provider);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Discussion

Override this method inherited from [`IOService`](../../DriverKit/ioservice.md).

Before terminating the object in `provider`, the system calls this method to stop the service associated with that object. Use your implementation of this method to stop all activity and put your driver in a quiescent state. If your driver has any in-progress asynchronous tasks, cancel those tasks and wait for DriverKit to call the associated cancellation handler before calling the super version of this method.

Call super at the end of your implementation. After you call `super`, it is a programmer error to access the provider object.

Don’t use this method to release your `ivars` structure; use the [`free`](./free.md) method instead.

## Parameters

- `provider`: The provider associated with the current service. This object is the same one that the system previously passed to your service’s [`Start`](./start.md) method.

## See Also

### Running the Driver Service
- [init](./init.md)
  Handles the basic initialization of the service.
- [Start](./start.md)
  Starts the current service and associates it with the specified provider.
- [free](./free.md)
  Performs any final cleanup for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/stop)*