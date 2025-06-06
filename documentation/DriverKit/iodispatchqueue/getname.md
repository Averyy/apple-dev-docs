# GetName

**Framework**: DriverKit  
**Kind**: method

Returns the name of the queue as a C string.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
const char * GetName();
```

#### Return Value

A C-string pointer to the queue’s internal storage.

#### Discussion

Returns a pointer to the queue’s name. This string is valid only while the queue is retained.

## See Also

- [OnQueue](iodispatchqueue/onqueue.md)
  Returns a Boolean value that indicates whether the current thread matches the dispatch queue’s thread.
- [IODispatchQueueName](iodispatchqueuename.md)
  A buffer for specifying the name of a dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchqueue/getname)*