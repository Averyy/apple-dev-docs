# Create

**Framework**: DriverKit  
**Kind**: method

Creates a new dispatch queue object.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static kern_return_t Create(const IODispatchQueueName name, uint64_t options, uint64_t priority, IODispatchQueue * * queue);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](error-codes.md).

#### Discussion

Creates a new dispatch queue object. All queues are currently serial, executing one block at time in FIFO order. The new object has retain count of 1 and should be released by the caller.

## Parameters

- `name`: The name of the queue.
- `options`: No options are currently defined. Specify   for this parameter.
- `priority`: No priorities are currently defined. Specify   for this parameter.
- `queue`: The created queue.

## See Also

- [init](iodispatchqueue/init.md)
  Initializes the dispatch queue object.
- [free](iodispatchqueue/free.md)
  Performs any final cleanup for the dispatch queue object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchqueue/create)*