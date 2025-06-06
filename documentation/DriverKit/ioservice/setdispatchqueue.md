# SetDispatchQueue

**Framework**: DriverKit  
**Kind**: method

Associates a custom dispatch queue with the service and assigns the specified name to it.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t SetDispatchQueue(const IODispatchQueueName name, IODispatchQueue * queue);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](error-codes.md).

#### Discussion

In your driver’s [`Start`](ioservice/start.md) method, call this method once for each unique queue name you designated in your class definition file. This method registers the dispatch queue with that name and assigns it to your service. When calling the methods of your service, DriverKit uses the appropriate dispatch queue. If DriverKit calls a method before you set the dispatch queue that method uses, the method runs on the default queue.

DriverKit creates a default dispatch queue for every service. To replace the default queue that DriverKit provides, call this method and specify `kIOServiceDefaultQueueName` for the `name` parameter.

## Parameters

- `name`: The name to assign to the queue. Use this name with the   macro to designate where you want the methods of your class to execute. Include that macro at the end of your method signature methods in the   file of your class.
- `queue`: The queue to associate with the service. The service retains the queue you provide.

## See Also

- [CopyDispatchQueue](ioservice/copydispatchqueue.md)
  Gets the dispatch queue with the specified name from the current service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservice/setdispatchqueue)*