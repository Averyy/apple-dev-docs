# IODispatchQueueName

**Framework**: DriverKit  
**Kind**: typealias

A buffer for specifying the name of a dispatch queue.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef char[256] IODispatchQueueName;
```

## See Also

- [GetName](iodispatchqueue/getname.md)
  Returns the name of the queue as a C string.
- [OnQueue](iodispatchqueue/onqueue.md)
  Returns a Boolean value that indicates whether the current thread matches the dispatch queue’s thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchqueuename)*