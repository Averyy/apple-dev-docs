# Create

**Framework**: DriverKit  
**Kind**: method

Creates a dispatch source that you use as a shared-memory data queue.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static kern_return_t Create(uint64_t queueByteCount, IODispatchQueue * queue, IODataQueueDispatchSource * * source);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. See [`Error Codes`](error-codes.md).

## Parameters

- `queueByteCount`: The size of the queue in bytes.
- `queue`: The dispatch queue to use for executing tasks. Note that the   and   handlers execute on the queue set for the target method of the associated   object, not this queue.
- `source`: A variable for storing the resulting dispatch source object. On success, the returned object has a retain count of 1, and you must release it when finished.

## See Also

- [init](iodataqueuedispatchsource/init.md)
  Handles the basic initialization of the dispatch source.
- [free](iodataqueuedispatchsource/free.md)
  Performs any final cleanup for the data-queue dispatch source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/create)*