# CopyDispatchQueue

**Framework**: DriverKit  
**Kind**: method

Gets the dispatch queue with the specified name from the current service.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t CopyDispatchQueue(const IODispatchQueueName name, IODispatchQueue * * queue);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](error-codes.md).

## Parameters

- `name`: The name you assigned to the dispatch queue. Specify   to retrieve the default dispatch queue.
- `queue`: A variable to use for storing the dispatch queue. On return, this parameter contains the retained queue, or   if no queue matches the specified name. You are responsible for releasing the returned dispatch queue.

## See Also

- [SetDispatchQueue](ioservice/setdispatchqueue.md)
  Associates a custom dispatch queue with the service and assigns the specified name to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservice/copydispatchqueue)*