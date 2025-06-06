# OnQueue

**Framework**: DriverKit  
**Kind**: method

Returns a Boolean value that indicates whether the current thread matches the dispatch queue’s thread.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool OnQueue();
```

#### Return Value

`true` if the current thread is the same thread that the dispatch queue is using to execute its task.

#### Discussion

Use this method to determine if your code is running on the same thread as the current dispatch queue.

## See Also

- [GetName](iodispatchqueue/getname.md)
  Returns the name of the queue as a C string.
- [IODispatchQueueName](iodispatchqueuename.md)
  A buffer for specifying the name of a dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchqueue/onqueue)*