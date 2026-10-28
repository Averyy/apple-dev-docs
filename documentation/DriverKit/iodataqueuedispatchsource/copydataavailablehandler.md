# CopyDataAvailableHandler

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

A private method that the dispatch source uses to detect enqueued data.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual kern_return_t CopyDataAvailableHandler(OSAction **action);
```

## Return Value

[`kIOReturnSuccess`](../kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../error-codes.md).

## See Also

### Performing Internal Tasks
- [CopyDataServicedHandler](./copydataservicedhandler.md)
  A private method that the dispatch source uses to detect dequeued data.
- [CopyMemory](./copymemory.md)
  A private method that the dispatch source uses to copy memory.
- [CheckForWork](./checkforwork.md)
  Checks for events to handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/copydataavailablehandler)*