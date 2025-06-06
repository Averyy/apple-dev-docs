# Stop

**Framework**: DriverKit  
**Kind**: method

Stops the service associated with the specified provider.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t Stop(IOService * provider);
```

## Mentions

- [Creating a Driver Using the DriverKit SDK](creating-a-driver-using-the-driverkit-sdk.md)

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](error-codes.md).

#### Discussion

Before terminating the object in `provider`, the system calls this method to stop the service associated with that object. Use your implementation of this method to stop all activity and put your driver in a quiescent state. If your driver has any in-progress asynchronous tasks, cancel those tasks and wait for DriverKit to call the associated cancellation handler before calling the `super` version of this method.

Call `super` at the end of your implementation. After you call `super`, it is a programmer error to access the `provider` object.

Don’t use this method to release your `ivars` structure; use the [`free`](ioservice/free.md) method instead.

## Parameters

- `provider`: The provider associated with the current service. This object is the same one that the system previously passed to your service’s   method.

## See Also

- [init](ioservice/init.md)
  Handles the basic initialization of the service.
- [Start](ioservice/start.md)
  Starts the current service and associates it with the specified provider.
- [free](ioservice/free.md)
  Performs any final cleanup for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservice/stop)*